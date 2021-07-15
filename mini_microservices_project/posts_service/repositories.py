import requests

post_list = [
]


def get_posts():
    return post_list


def create_post(title):
    id = post_list[-1]['id']+1 if post_list else 1
    new_post = {
        'id': id,
        'title': title
    }
    post_list.append(new_post)
    event = {
        'event_type': 'POST_CREATED',
        'data': new_post
    }
    requests.post('http://localhost:5004/events', json=event)
    return new_post