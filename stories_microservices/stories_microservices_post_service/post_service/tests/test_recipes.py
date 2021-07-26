from ..models import Recipe

def test_get_request_status_code(client):
    response = client.get('/recipes/')
    assert response.status_code == 200


def test_get_request_body(client):
    recipe = Recipe.query.first()
    response = client.get('/recipes/')
    assert response.json[0]['title'] == recipe.title


def test_post_request(client):
    data = {
        "category_id": 1,
        "description": "sdjkfnsjf",
        "short_description": "slkdnklsd",
        "title": "lsdknfdlkf"
    }
    res = client.post('/recipes/', json=data)
    assert res.status_code == 201
    assert res.json['title'] == data['title']

