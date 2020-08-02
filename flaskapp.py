######importing
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

#from business_eda import EdaBuilder
from business_actor import ActorBusiness
from business_cause import CauseBusiness
from business_vehicle import VehiclesBusiness
from business_geodata import GeodataBusiness
from business_accident import AccidentBusiness

#####init
application = app = Flask(__name__)
api = Api(app)

#####body
class WelcomeServices(Resource):
    def get(self):
        return 'It works!'

class AccidentServices(Resource):
    def get(self):
        return AccidentBusiness().GetAccidents()

class ActorServices(Resource):
    def get(self):
        return ActorBusiness().GetActors()

class CauseServices(Resource):
    def get(self):
        return CauseBusiness().GetCauses()

class VehicleServices(Resource):
    def get(self):
        return VehiclesBusiness().GetVehicles()

class GeodataServices(Resource):
    def get(self):
        return GeodataBusiness().GetGeodata()

#####resources
api.add_resource(WelcomeServices, '/')

#accident
api.add_resource(AccidentServices, '/accident')
##actor
api.add_resource(ActorServices, '/actor')
##cause
api.add_resource(CauseServices, '/cause')
##vehicle
api.add_resource(VehicleServices, '/vehicle')
##geodata
api.add_resource(GeodataServices, '/geodata')


######environment
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
if __name__ == '__main__':
    app.run(debug = True)