from bottle import route, response, request, abort
from bottle import get

from util import *

@route('/', method='GET')
def home():
    abort(418)

@get('/api/')
def api_home():
    return test_method()
