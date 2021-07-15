import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from flask import jsonify, request

from app import app

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


@app.route('/events', methods=['POST'])
def posts():
    event = dict(request.json or request.form)
    res = requests.post('http://localhost:5000/events', json=event)
    res = requests.post('http://localhost:5001/events', json=event)
    res = requests.post('http://localhost:5003/events', json=event)
    return jsonify({'message': 'success'}), 200
