# -*- coding: utf-8 -*-

from bottle import route, run
import generator

@route('/')
def top():
    return generator.top()

@route('/login')
def login():
    pass

run(host='0.0.0.0', port=80)
