from data_connection import ConnectionClass

class EdaBuilder:
    def Accidents(self):

        query = 'SELECT * from accidents limit 10'
        headers = 'CODIGO_SINIESTRO', 'FECHA', 'HORA', 'GRAVEDAD', 'CLASE', 'CHOQUE_CON','OBJETO_FIJO', 'DIRECCION', 'TOTAL_MUERTOS', 'TOTAL_HERIDOS', 'LOCALIDAD', 'DISENO_LUGAR'
        
        connection = ConnectionClass()
        response = connection.JsonFromQuery(query, headers)
        
        return response