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
    return new_post