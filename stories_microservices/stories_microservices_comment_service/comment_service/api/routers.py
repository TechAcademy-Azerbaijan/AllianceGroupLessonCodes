from http import HTTPStatus
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from flasgger import swag_from

from ..app import app
from ..config.extentions import mydb
from ..schemas.schema import CommentSchema
from bson.objectid import ObjectId

'''
Comment()
post_id =
content =
parent_comment =
sub_comments = [
]
# owner =
'''


@app.route('/posts/<int:id>/comments', methods=['GET', 'POST'])
@jwt_required()
def comments(id):
    if request.method == 'POST':
        data = dict(request.json or request.form)
        try:
            serializer = CommentSchema().load(data)
            serializer['user_id'] = get_jwt_identity()
            serializer['post_id'] = id
            mycol = mydb["comments_tb"]
            parent_comment_id = serializer.get('parent_comment')

            created_comment = mycol.insert_one(dict(serializer))

            serializer['_id'] = str(created_comment.inserted_id)
            if parent_comment_id:
                x = mycol.update_one({'_id': ObjectId(parent_comment_id)},
                                     {'$push': {'sub_comments': dict(serializer)}})
            return jsonify(serializer)
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST

    mycol = mydb["comments_tb"]
    comments = mycol.find({'parent_comment': None})
    return CommentSchema(many=True).jsonify(comments), HTTPStatus.OK
