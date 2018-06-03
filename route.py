from builtins import print

from bottle import route, response, request, abort, redirect
from bottle import get, post
import json

from util import *

@route('/', method='GET')
def home():
    abort(418)

@get('/api/')
def api_home():
    return test_method()

@get('/pair/<id>')
def get_pair(id):

    return get_pair_logic(id)


@post('/pair/update/status')
def post_pair():
    print(request.json)
    ja = request.json['ja']
    other = request.json['other']
    post_and_fetch_num((ja, other))