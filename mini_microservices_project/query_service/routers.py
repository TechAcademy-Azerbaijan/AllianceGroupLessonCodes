from flask import jsonify, request
from app import app
from repositories import get_posts, create_post, created_comment


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    post_list = get_posts()
    return jsonify(post_list), 200


@app.route('/events', methods=['POST'])
def events():
    event = dict(request.json or request.form)
    if event['event_type'] == 'POST_CREATED':
        create_post(post_data=event['data'])
    if event['event_type'] == 'COMMENT_CREATED':
        created_comment(comment_data=event['data'])
    return jsonify({'message': 'success'}), 200
