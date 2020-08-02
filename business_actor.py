from data_connection import ConnectionClass

class ActorBusiness:
    def GetActors(self):
        query = 'SELECT * from actors limit 100'
        headers = 'CODIGO_SINIESTRO', 'FECHA', 'CONDICION', 'ESTADO', 'EDAD', 'SEXO', 'VEHICULO'
        return ConnectionClass().JsonFromQuery(query, headers)