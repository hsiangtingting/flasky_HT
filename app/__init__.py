from flask import Flask
<<<<<<< HEAD
from .routes.cat_routes import cats_bp
=======
from .db import db, migrate
from .models.cat import Cat
from .routes.cat_routes import cats_bp
import os
>>>>>>> upstream/c24-live-code

def create_app(config = None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

<<<<<<< HEAD
    app.config[]

=======
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)
>>>>>>> upstream/c24-live-code

    app.register_blueprint(cats_bp)

    return app