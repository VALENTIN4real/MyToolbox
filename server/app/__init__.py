import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import routes
from .database import db

def create_app(test_config=None):
    # Crée et configure l'application
    app = Flask(
        __name__,
        instance_path=os.path.join(os.path.abspath(os.path.dirname(__file__)), "../instance"),
        instance_relative_config=True
    )

    # Exemple de configuration
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'toolbox.sqlite'),
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///toolbox.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Assure que le dossier d'instance existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    db.init_app(app)
    routes.init_routes(app)

    return app