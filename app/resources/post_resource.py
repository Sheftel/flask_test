from flask_restful import marshal

from app.marshalling import PostRequestParser, PostSchema
from app.extensions import db
from app.models import Post

class PostResource:
    def put(self, post_id):
        post = Post.query.get(post_id)
        if post is None:
            return {"message": "Post not found"}, 404

        post_parser = PostRequestParser()
        data = post_parser.parse_args()
        post.title = data.items('title')
        post.content = data.items('content')
        db.session.commit()

        return marshal(post, PostSchema)

    def get(self, post_id):
        post = Post.query.get(post_id)
        if post is None:
            return {"message": "Post not found"}, 404

        return marshal(post, PostSchema)
    def delete(self, post_id):
        post = Post.query.get(post_id)
        if post is None:
            return {"message": "Post not found"}, 404

        Post.query.delete()
        db.session.commit()

        return {"Post successfully deleted"}, 200
