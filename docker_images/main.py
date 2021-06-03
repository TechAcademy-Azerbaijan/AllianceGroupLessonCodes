from flask import Flask
import redis
import os


if os.getenv('DEBUG'):
    r = redis.Redis(host='redisdb', port=6379, db=0)
else:
    r = redis.Redis(host='localhost', port=6380, db=0)

app = Flask(__name__)

@app.route('/')
def home():
    return f'This page called {r.incr("i")}'


@app.route('/about')
def about():
    return 'About Page'

