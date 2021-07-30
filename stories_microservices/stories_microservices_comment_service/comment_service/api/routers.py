from http import HTTPStatus
from flask import request, jsonify
from marshmallow import ValidationError
from flasgger import swag_from

from ..app import app
from ..models import Comment
from ..schemas.schema import CommentSchema


@app.route('/posts/<int:id>/comments', methods=['GET', 'POST'])
def comments(id):
    if request.method == 'POST':
        data = dict(request.json or request.form)
        try:
            serializer = CommentSchema().load(data)
            print(serializer)
            content = serializer.get('content')
            parent_comment = serializer.get('parent_comment')
            user_id = 1
            comment = Comment(content=content, user_id=user_id, post_id=id)
            comment.save()
            if parent_comment:
                pass
            return CommentSchema().jsonify(parent_comment), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST


    # recipes = Recipe.query.filter_by(is_published=True)
    # return RecipeSchema(many=True).jsonify(recipes), HTTPStatus.OK
