from flask import render_template, url_for
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from sqlalchemy.sql import func
from .config.extentions import db, login_manager
from .publisher import Publish
from .utils.tokens import generate_confirmation_token


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class SaveMixin(object):
    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(),
                           server_onupdate=func.now(), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(UserMixin, SaveMixin, db.Model):
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(254), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)

    is_active = db.Column(db.Boolean, nullable=False, default=False)
    date_joined = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    bio = db.Column(db.TEXT, nullable=True)
    gender = db.Column(db.Boolean, nullable=False, default=True)
    image = db.Column(db.String(500), nullable=True)
    is_superuser = db.Column(db.Boolean, nullable=False, default=False)

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __init__(self, *args, **kwargs):
        kwargs['password'] = generate_password_hash(kwargs['password'])
        super(User, self).__init__(*args, **kwargs)

    def send_confirmation_mail(self):
        token = generate_confirmation_token(self.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('confirmation_email.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        Publish(event_type='send_mail', data={
            'body': html,
            'subject': subject,
            'recipients': [self.email]
        })

