from marshmallow import validates, ValidationError
from marshmallow.fields import Integer, String

from ..config.extentions import ma
from ..models import Recipe, Category


class RecipeSchema(ma.SQLAlchemyAutoSchema):
    owner_id = Integer(dump_only=True)
    slug = String(dump_only=True)

    class Meta:
        model = Recipe
        include_fk = True
        load_instance = True

    @validates('category_id')
    def validate_category_id(self, value):
        if not Category.query.filter_by(id=value).first():
            raise ValidationError(f"Category not found with {value} pk")
        return True
