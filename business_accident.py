from data_connection import ConnectionClass

class AccidentBusiness:
    def GetAccidents(self):
        query = 'SELECT * from accidents limit 100'
        headers = 'CODIGO_SINIESTRO', 'FECHA', 'HORA', 'GRAVEDAD', 'CLASE', 'CHOQUE_CON','OBJETO_FIJO', 'DIRECCION', 'TOTAL_MUERTOS', 'TOTAL_HERIDOS', 'LOCALIDAD', 'DISENO_LUGAR'
        return ConnectionClass().JsonFromQuery(query, headers)