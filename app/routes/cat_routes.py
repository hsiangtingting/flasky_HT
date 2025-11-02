from flask import Blueprint, abort, make_response
from app.models.cat import cats

cats_bp = Blueprint("cat_bp", __name__, url_prefix="/cats")

@cats_bp.get("")
def get_all_cats():
    result_list = []

    for cat in cats:
        result_list.append(dict(
            id=cat.id,
            name=cat.name,
            color=cat.color,
            personality=cat.personality
        ))

    return result_list

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


def validate_cat(id):
    try:
        id = int(id)
    except ValueError:
        invalid = {"message": f"Cat id ({id}) is invalid."}
        abort(make_response(invalid, 400))

    for cat in cats:
        if cat.id == id:
            return cat

    not_found= {"message": f"Cat id ({id}) not found."}
    abort(make_response(not_found, 404))

    