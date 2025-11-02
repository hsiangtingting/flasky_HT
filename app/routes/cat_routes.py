<<<<<<< HEAD
from flask import Blueprint, abort, make_response
from app.models.cat import cats

cats_bp = Blueprint("cat_bp", __name__, url_prefix="/cats")

@cats_bp.get("")
def get_all_cats():
=======
from flask import abort, Blueprint, make_response, request, Response
from ..models.cat import Cat
from ..db import db

cats_bp = Blueprint("cat_bp", __name__, url_prefix="/cats")

@cats_bp.post("")
def create_cat():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body["color"]
    personality = request_body["personality"]

    new_cat = Cat(
        name=name,
        color=color,
        personality=personality
    )
    db.session.add(new_cat)
    db.session.commit()

    cat_response = dict(
        id=new_cat.id,
        name=new_cat.name,
        color=new_cat.color,
        personality=new_cat.personality
    )

    return cat_response, 201

@cats_bp.get("")
def get_all_cats():
    query = db.select(Cat)
    name_param = request.args.get("name")
    if name_param:
        # find exact match for name
        query = query.where(Cat.name == name_param)

    color_param = request.args.get("color")
    if color_param:
        query = query.where(Cat.color.ilike(f"%{color_param}%"))

    personality_param = request.args.get("personality")
    if personality_param:
        query = query.where(Cat.personality.ilike(f"%{personality_param}%"))

    query = query.order_by(Cat.id)

    cats = db.session.scalars(query)
>>>>>>> upstream/c24-live-code
    result_list = []

    for cat in cats:
        result_list.append(dict(
            id=cat.id,
            name=cat.name,
            color=cat.color,
            personality=cat.personality
        ))

    return result_list

<<<<<<< HEAD
        # result_list.append({
        #     "id":cat.id,
        #     "name":cat.name,
        #     "color":cat.color,
        #     "personality":cat.personality
        # })

        #different syntax to make a dict

@cats_bp.get("/<id>")
def get_single_cat(id):

    # validate_cat(id)

    # for cat in cats:
    #     if cat.id == id:
    #         return dict(
    #         id=cat.id,
    #         name=cat.name,
    #         color=cat.color,
    #         personality=cat.personality
    #     )
#-- after refactoring --
    cat = validate_cat(id)
    cat_dict = dict(
            id=cat.id,
            name=cat.name,
            color=cat.color,
            personality=cat.personality
    )
    return cat_dict

=======
@cats_bp.get("/<id>")
def get_single_cat(id):
    cat = validate_cat(id)
    cat_dict = dict(
        id=cat.id,
        name=cat.name,
        color=cat.color,
        personality=cat.personality
    )

    return cat_dict
>>>>>>> upstream/c24-live-code

def validate_cat(id):
    try:
        id = int(id)
    except ValueError:
        invalid = {"message": f"Cat id ({id}) is invalid."}
        abort(make_response(invalid, 400))

<<<<<<< HEAD
    for cat in cats:
        if cat.id == id:
            return cat

    not_found= {"message": f"Cat id ({id}) not found."}
    abort(make_response(not_found, 404))

    
=======
    query = db.select(Cat).where(Cat.id == id)
    cat = db.session.scalar(query)
    if not cat:    
        not_found = {"message": f"Cat with id ({id}) not found."}
        abort(make_response(not_found, 404))

    return cat

@cats_bp.put("/<id>")
def replace_cat(id):
    cat = validate_cat(id)

    request_body = request.get_json()
    cat.name = request_body["name"]
    cat.color = request_body["color"]
    cat.personality = request_body["personality"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@cats_bp.delete("/<id>")
def delete_cat(id):
    cat = validate_cat(id)

    db.session.delete(cat)
    db.session.commit()

    return Response(status=204, mimetype="application/json")
>>>>>>> upstream/c24-live-code
