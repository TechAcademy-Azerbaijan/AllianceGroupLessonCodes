from http import HTTPStatus
from flask import request, jsonify
from marshmallow import ValidationError
# from flasgger import swag_from

from ..app import app
from ..schemas.schema import SubscriberSchema
# from ..tasks import send_mail_to_subscribers


@app.route('/subscribe/', methods=['POST'])
def subscribe():
    # send_mail_to_subscribers()
    data = dict(request.json or request.form)
    try:
        subscriber = SubscriberSchema().load(data)
        subscriber.save()
        return SubscriberSchema().jsonify(subscriber), HTTPStatus.CREATED
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST

