post_list = [
]


def get_posts():
    return post_list


def create_post(post_data):
    post_data['comments'] = []
    post_list.append(post_data)


def created_comment(comment_data):
    post_id = comment_data.pop('post_id')
    for post in post_list:
        if post_id == post['id']:
            post['comments'].append(comment_data)
