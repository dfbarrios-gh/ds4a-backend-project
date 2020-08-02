from data_connection import ConnectionClass

class AccidentBusiness:
    def GetAccidents(self):
        query = 'SELECT * from accidents limit 100'
        headers = 'CODIGO_SINIESTRO', 'FECHA', 'HORA', 'GRAVEDAD', 'CLASE', 'CHOQUE_CON','OBJETO_FIJO', 'DIRECCION', 'TOTAL_MUERTOS', 'TOTAL_HERIDOS', 'LOCALIDAD', 'DISENO_LUGAR'
        return ConnectionClass().JsonFromQuery(query, headers)

    def GetAccidentsBySubtown(self):
        query = "select a.LOCALIDAD as Subtown, count(g.Identificador) as NumberOfAccidents from accidents a inner join geodata g on a.CODIGO_SINIESTRO = g.Identificador group by a.LOCALIDAD order by NumberOfAccidents desc;"
        headers = 'Subtown','NumberOfAccidents'
        return ConnectionClass().JsonFromQuery(query, headers)