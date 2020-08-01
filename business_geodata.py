from data_connection import ConnectionClass

class GeodataBusiness:
    def GetGeodata(self):
        query = 'SELECT * from geodata'
        headers = 'Identificador','Direccion','municipio','estado','dirtrad','diraprox','tipo_direccion','codloc','localidad','codupz','nomupz','codseccat','nomseccat','cpocodigo','mancodigo','lotcodigo','longitude','latitude'
        return ConnectionClass().JsonFromQuery(query, headers)
