comment_list = [
    {
        'comment_id': 1,
        'content': 'Comment 1',
        'post_id': 1
    },
    {
        'comment_id': 2,
        'content': 'Comment 2',
        'post_id': 1
    },
    {
        'comment_id': 3,
        'content': 'Comment 3',
        'post_id': 2
    }
]


def get_comments(post_id):
    comments = []
    for comment in comment_list:
        if comment['post_id'] == post_id:
            comments.append(comment)
    return comments


def create_comment(post_id, content):
    new_comment = {
        'comment_id': comment_list[-1]['comment_id']+1,
        'content': content,
        'post_id': post_id
    }
    comment_list.append(new_comment)
    return new_comment
