from flask_login import UserMixin
from slugify import slugify
from sqlalchemy.sql import func

from .cache import Cache
from .config.extentions import db


class Comment(db.Document):
    post_id = db.IntField()
    user_id = db.IntField()
    content = db.StringField(max_length=255,)
    comments = db.ListField(db.DictField())
