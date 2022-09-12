# loadbalancer.py

import random

import requests
from flask import Flask, request

loadbalancer = Flask(__name__)

NODE_BACKENDS = ['192.168.1.35:80', '192.168.1.34:80', '192.168.1.32:80', '192.168.1.30:80', '192.168.1.31:80', '192.168.1.29:80']


@loadbalancer.route('/')
def router():
    host_header = request.headers['Host']
    if host_header == 'www.mylb.com':
        response = requests.get(f'http://{random.choice(NODE_BACKENDS)}')
        return response.content, response.status_code
    else:
        return 'Not Found', 404

