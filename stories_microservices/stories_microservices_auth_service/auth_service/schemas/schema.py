from marshmallow import validates, ValidationError, fields, validate, validates_schema

from ..config.extentions import ma
from ..models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    confirm_password = ma.String(load_only=True, required=True, validate=[validate.Length(min=8, max=20)])
    password = ma.String(load_only=True, required=True, validate=[validate.Length(min=8, max=20)])

    class Meta:
        model = User
        include_fk = True
        load_instance = True
        exclude = ('is_superuser', 'is_active', 'date_joined', )

    @validates_schema
    def validate_confirm_password(self, data, **kwargs):
        if not data["password"] == data["confirm_password"]:
            raise ValidationError('Confirm password is not same with password')

    @validates('email')
    def validate_email(self, value):
        if User.query.filter_by(email=value).first():
            raise ValidationError("Email field must be unique!")
        return True

    @validates('username')
    def validate_username(self, value):
        if User.query.filter_by(username=value).first():
            raise ValidationError("Username field must be unique!")
        return True


class LoginSchema(ma.Schema):
    username = ma.String(required=True, validate=[validate.Length(min=3, max=20)])
    password = ma.String(required=True, validate=[validate.Length(min=8, max=20)])

    # @validates('category_id')
    # def validate_category_id(self, value):
    #     if not Category.query.filter_by(id=value).first():
    #         raise ValidationError(f"Category not found with {value} pk")
    #     return True
