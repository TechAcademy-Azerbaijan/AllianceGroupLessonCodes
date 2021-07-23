from datetime import timedelta

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from ..app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://auth_user:12345@localhost:5433/auth_db_name"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
ma = Marshmallow(app)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "alksdnakndsklndnlknsdn23u39204903ur9230jnf9nwndfisn"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)

