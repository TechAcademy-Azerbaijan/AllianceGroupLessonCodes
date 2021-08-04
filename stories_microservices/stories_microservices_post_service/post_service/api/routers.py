from http import HTTPStatus
from flask import request, jsonify
from marshmallow import ValidationError
from flasgger import swag_from

from ..api import api
from ..models import Recipe
from ..schemas.schema import RecipeSchema


@api.route('/recipes', methods=['GET', 'POST'])
@swag_from('api-docs/recipes.yml', methods=['GET',])
@swag_from('api-docs/post_recipe.yml', methods=['POST',])
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
