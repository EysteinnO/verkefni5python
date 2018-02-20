# -*- coding: cp1252 -*-
from bottle import *
import os
import json
import requests

api_token = 'api'
response = requests.get('http://apis.is/concerts')

data = response.json()
print(type(data))
print(data)

with open('bekkur.json') as json_data:
    data = json.load(json_data)
    #print(data)    

@route('/staticskrar/<skra>')
def staticskrar(skra):
    return static_file(skra, root='./myndir')
    
@route('/')
def index():
    return template('index.tpl', data = data)
    
@route('/nemandi/<id>')
def index(id):
        return template('nemandi.tpl', id=id, data=data)

@error(404)
def villa(error):
    return "<br><h1>Þessi síða er ekki til</h1>"

run()
#run(host='0.0.0.0', port=os.environ.get('PORT'))
