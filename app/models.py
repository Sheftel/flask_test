from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .extensions import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    title = Column(String(50), nullable=False)
    content = Column(String(250), nullable=False)

    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Post %r>' % self.title


def init_db():
    if db.session.query(Post.id).first() is None:
        db.session.add(Post(title='First Post', content='Content of first post'))
        db.session.add(Post(title='Second Post', content='Content of second post'))
    db.session.commit()

