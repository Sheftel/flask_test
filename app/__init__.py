import config
from flask import Flask
from . import views
from .extensions import db, migrate


def create_app():
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config.DevelopmentConfig())
    register_extensions(app)
    register_blueprints(app)
    with app.app_context():
        db.create_all()
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    app.register_blueprint(views.bp)
    return None
