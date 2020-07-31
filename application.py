#importing
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

#custom
from connection import ConnectionClass

application = app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        myConnectionClass = ConnectionClass()
        val = myConnectionClass.conectar()
        #print(val)
        #return {'about':val}
        return val

api.add_resource(HelloWorld, '/')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

if __name__ == '__main__':
    app.run(debug = True)