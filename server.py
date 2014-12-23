#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask.ext import restful

from cancelamento_de_disciplina import gen

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self, nome):
        
    	filename = gen(nome, nome, nome)

        return {'hello': filename}


api.add_resource(HelloWorld, '/<string:nome>')

if __name__ == '__main__':
    app.run(debug=True)