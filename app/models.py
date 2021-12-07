from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func

db = SQLAlchemy()


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
