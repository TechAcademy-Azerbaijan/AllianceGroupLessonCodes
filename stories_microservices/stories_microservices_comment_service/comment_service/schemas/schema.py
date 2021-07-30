from marshmallow import validates, ValidationError, validate
from marshmallow.fields import Integer, String, Nested, Method

from ..config.extentions import ma

from ..models import Comment


class CommentSchema(ma.Schema):
    id = String(dump_only=True)
    post_id = Integer(dump_only=True)
    user_id = Integer(dump_only=True)
    content = String(required=True, validate=[validate.Length(min=1, max=255)])
    parent_comment = String(load_only=True)
    comments = Method("get_comments")

    def get_comments(self, obj):
        print(obj.comments)
        return obj.comments