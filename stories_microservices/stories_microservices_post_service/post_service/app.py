from flask import Flask


app = Flask(__name__)

from .config.extentions import *
from .models import *
from .api.routers import api

app.register_blueprint(api, url_prefix='/api/v1.0/posts')
