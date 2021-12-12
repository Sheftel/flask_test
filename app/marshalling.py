from flask_restful import fields
from flask_restful.reqparse import RequestParser


PostSchema = {
    'id': fields.Integer(default=None),
    'created': fields.DateTime,
    'title': fields.String,
    'content': fields.String
}


class PostRequestParser(RequestParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_argument(
            'title', type=str, required=True, nullable=False
        )
        self.add_argument(
            'content', type=str, required=True, nullable=False
        )

