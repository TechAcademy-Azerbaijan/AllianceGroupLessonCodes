from http import HTTPStatus
from flask import request, jsonify
from marshmallow import ValidationError

from ..app import app
from ..models import Recipe
from ..schemas.schema import RecipeSchema


@app.route('/recipes/', methods=['GET', 'POST'])
def recipes():
    if request.method == 'POST':
        recipe_data = dict(request.json or request.form)
        try:
            recipe = RecipeSchema().load(recipe_data)
            recipe.owner_id = 1
            recipe.save()
            return RecipeSchema().jsonify(recipe), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST


    recipes = Recipe.query.filter_by(is_published=True)
    return RecipeSchema(many=True).jsonify(recipes), HTTPStatus.OK