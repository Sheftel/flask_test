from flask_restful import Api
from .resources.post_resource import PostResource


def init_routes(app):
    api = Api(app)
    api.add_resource(PostResource, '/post/<int:post_id>')
