from bottle import route, response, request, abort, redirect
from bottle import get, post

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
    ja = request.forms.ja
    other = request.forms.other

    return ja, other

    #id = post_and_fetch_num((ja, other))
    #return redirect('/pair/{}'.format(id))
