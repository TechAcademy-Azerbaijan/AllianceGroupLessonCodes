from ..models import Recipe, Category, User


def test_get_request_status_code(client):
    response = client.get('/recipes/')
    assert response.status_code == 200


# def test_get_request_body(client):
#     cat = Category(title='cat', image='image.png')
#     recipe = Recipe.query.first()
#     response = client.get('/recipes/')
#     assert response.json[0]['title'] == recipe.title


def test_post_request(client):
    # cat = Category(title='cat', image='image.png')
    # cat.save()
    # user = User(id=1, email='idris.sabanli@gmail.com', username='idris')
    # user.save()
    data = {
        "category_id": 1,
        "description": "sdjkfnsjf",
        "short_description": "slkdnklsd",
        "title": "lsdknfdlkf"
    }
    res = client.post('/recipes/', json=data)
    print(res.data)
    assert res.status_code == 201
    assert res.json['title'] == data['title']

