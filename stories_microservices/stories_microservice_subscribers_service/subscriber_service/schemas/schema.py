from marshmallow import validates, ValidationError
from marshmallow.fields import Integer, String

from ..config.extentions import ma
from ..models import Subscriber


class SubscriberSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Subscriber
        include_fk = True
        load_instance = True
        exclude = ('is_active',)

    @validates('email')
    def validate_email(self, value):
        if Subscriber.query.filter_by(email=value).first():
            raise ValidationError("Email field must be unique!")
        return True


