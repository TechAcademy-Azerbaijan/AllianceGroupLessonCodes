import os
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from ..app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://post_user:12345@localhost:5432/post_db_names"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
ma = Marshmallow(app)
swagger = Swagger(app)


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
