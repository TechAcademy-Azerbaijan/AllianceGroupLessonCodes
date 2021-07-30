from flask import Flask


app = Flask(__name__)

from .api.routers import *
from .config.extentions import *
from .models import *

