#importing
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from business_eda import EdaBuilder

#init
application = app = Flask(__name__)
api = Api(app)

#body
class Welcome(Resource):
    def get(self):
        eda = EdaBuilder()
        response = eda.Accidents()
        return response

#resources
api.add_resource(Welcome, '/')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


#environment
if __name__ == '__main__':
    app.run(debug = True)