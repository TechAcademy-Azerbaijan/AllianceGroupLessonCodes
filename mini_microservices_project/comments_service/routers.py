from flask import jsonify, request
from app import app
from repositories import get_comments, create_comment


@app.route('/posts/<int:post_id>/comments/', methods=['GET', 'POST'])
def comments(post_id):
    if request.method == "POST":
        comment_data = dict(request.json or request.form)
        new_comment = create_comment(post_id, comment_data['content'])
        return jsonify(new_comment), 201
    comment_list = get_comments(post_id)
    return jsonify(comment_list), 200
