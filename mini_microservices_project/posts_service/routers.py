from flask import jsonify, request
from app import app
from repositories import get_posts, create_post


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_data = dict(request.json or request.form)
        if post_data.get('title') and 0<len(post_data['title'])<255:
            new_post = create_post(title=post_data['title'])
            return jsonify(new_post), 201
    post_list = get_posts()
    return jsonify(post_list), 200


@app.route('/events', methods=['POST'])
def events():
    return jsonify({'message': 'success'}), 200