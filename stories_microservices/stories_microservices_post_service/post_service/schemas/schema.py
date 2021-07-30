from marshmallow import validates, ValidationError
from marshmallow.fields import Integer, String, Nested, Method

from ..config.extentions import ma
from ..models import Recipe, Category, User


class UserSchema(ma.SQLAlchemyAutoSchema):
    full_name = Method("get_full_name")

    class Meta:
        model = User
        include_fk = True
        load_instance = True
        exclude = ('is_superuser', 'is_active', 'date_joined',)

    def get_full_name(self, obj):
        return obj.get_full_name



class RecipeSchema(ma.SQLAlchemyAutoSchema):
    owner_id = Integer(dump_only=True)
    slug = String(dump_only=True)
    owner = Nested(UserSchema, dump_only=True)

    class Meta:
        model = Recipe
        include_fk = True
        load_instance = True

    @validates('category_id')
    def validate_category_id(self, value):
        if not Category.query.filter_by(id=value).first():
            raise ValidationError(f"Category not found with {value} pk")
        return True
