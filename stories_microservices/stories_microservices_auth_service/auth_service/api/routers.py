from http import HTTPStatus
from flask import request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from marshmallow import ValidationError

from ..app import app
from ..models import User
from ..schemas.schema import UserSchema, LoginSchema


@app.route('/register/', methods=['POST'])
def register():
    user_data = dict(request.json or request.form)
    try:
        user = UserSchema().load(user_data)
        user.save()
        return UserSchema().jsonify(user), HTTPStatus.CREATED
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST


@app.route("/login", methods=["POST"])
def login():
    user_login_info = dict(request.json or request.form)
    try:
        user_data = LoginSchema().load(user_login_info)
        user = User.query.filter_by(username=user_data['username']).first()
        if user and check_password_hash(user.password, user_data['password']):
            user_info = UserSchema().dump(user)
            user_info['access_token'] = create_access_token(identity=user.id)
            user_info['refresh_token'] = create_refresh_token(identity=user.id)
            return jsonify(user_info)
        else:
            return jsonify({'message': 'Invalid credentials'}), HTTPStatus.UNAUTHORIZED
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id).first()
    return UserSchema().jsonify(user), 200

