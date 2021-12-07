import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import Post, db
from . import views


def create_app():
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config.DevelopmentConfig())
    db.app = app
    db.init_app(app)

    app.register_blueprint(views.bp)
    db.create_all()
    if db.session.query(Post.id).first() is None:
        db.session.add(Post(title='First Post', content='Content of first post'))
        db.session.add(Post(title='Second Post', content='Content of second post'))
    db.session.commit()

    return app


