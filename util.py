import os
import sqlite3
import json


def test_method():
    return os.listdir('../')

def get_pair_logic(id):

    conn = sqlite3.connect('./test.db')
    cur = conn.cursor()

    c = cur.execute('select ja, other from phrase where id = {}'.format(id))
    pair = cur.fetchone()
    print(pair)
    conn.close()

    dic = {}
    dic['ja'] = pair[0]
    dic['other'] = pair[1]

    return json.dumps({'result':dic})

def post_and_fetch_num(pair):

    conn = sqlite3.connect('./test.db')
    cur = conn.cursor()

    c = cur.execute('select count(*) from phrase')
    fetch_id = cur.fetchone()[0]
    print(fetch_id)

    cur.execute("insert into phrase values({}, '{}', '{}')".format(fetch_id+1, pair[0], pair[1]))
    conn.commit()

    conn.close()

    return fetch_id + 1
