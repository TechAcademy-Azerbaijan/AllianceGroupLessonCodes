from marshmallow import validates, ValidationError, validate
from marshmallow.fields import Integer, String, Nested, Method

from ..config.extentions import ma, mydb


class CommentSchema(ma.Schema):
    id = String(dump_only=True)
    post_id = Integer(dump_only=True)
    user_id = Integer(dump_only=True)
    content = String(required=True, validate=[validate.Length(min=1, max=255)])
    parent_comment = String()
    comments = Method("get_comments")

    def get_comments(self, obj):
        return obj['sub_comments']


    # def save(self):
    #     mycol = mydb["comments_tb"]
    #     created_comment = mycol.insert_one(dict(self.load_fields))
    #     inserted_data = self.load_fields
    #     inserted_data['_id'] = str(created_comment.inserted_id)
    #     return inserted_data

