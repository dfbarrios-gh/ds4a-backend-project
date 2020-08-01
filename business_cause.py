from data_connection import ConnectionClass

class CauseBusiness:
    def GetCauses(self):
        query = 'SELECT * from causes'
        headers = 'CODIGO_SINIESTRO', 'FECHA', 'CODIGO_CAUSA', 'DESCRIPCION', 'CODIGO_CAUSA2', 'DESCRIPCION2'
        return ConnectionClass().JsonFromQuery(query, headers)