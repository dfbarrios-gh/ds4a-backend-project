from data_connection import ConnectionClass

class AccidentBusiness:
    def GetAccidents(self):
        query = 'SELECT * from accidents limit 100'
        headers = 'CODIGO_SINIESTRO', 'FECHA', 'HORA', 'GRAVEDAD', 'CLASE', 'CHOQUE_CON','OBJETO_FIJO', 'DIRECCION', 'TOTAL_MUERTOS', 'TOTAL_HERIDOS', 'LOCALIDAD', 'DISENO_LUGAR'
        return ConnectionClass().JsonFromQuery(query, headers)

    def GetAccidentsBySubtown(self):
        query = "select a.LOCALIDAD as Subtown, count(g.Identificador) as NumberOfAccidents from accidents a inner join geodata g on a.CODIGO_SINIESTRO = g.Identificador group by a.LOCALIDAD order by NumberOfAccidents desc;"
        headers = 'Subtown','NumberOfAccidents'
        jsonstring= ConnectionClass().JsonFromQuery(query, headers)
        return jsonstring

    def GetAccidentsPerDayOfWeek(self):
        query =  """select to_char(DATEGFORMAT, 'DAY') as DayOfWeek, count(CODIGO_SINIESTRO) AS NumberOfAccidents from 
        ( select TO_TIMESTAMP(HORA_FORMT, 'DD/MM/YYYY HH24:MI:SS') AS DATEGFORMAT, CODIGO_SINIESTRO FROM (select FECHA || ' ' || HORA as HORA_FORMT, CODIGO_SINIESTRO from accidents) as sq) AS sr
        group by DayOfWeek""" 
        headers = 'DayOfWeek','NumberOfAccidents'
        jsonstring= ConnectionClass().JsonFromQuery(query, headers)
        return jsonstring

    def GetAccidentsPerHourOfDay(self):
        query = "select COUNT(CODIGO_SINIESTRO) AS NumberOfAccidents, extract(hour from DT_HORA_DIA) as Hour from (select TO_TIMESTAMP(HORA_FORMT, 'DD/MM/YYYY HH24:MI:SS') AS DT_HORA_DIA, CODIGO_SINIESTRO FROM (select FECHA || ' ' || HORA as HORA_FORMT, CODIGO_SINIESTRO from accidents) as sq) so group by HOUR order by Hour"
        headers = 'NumberOfAccidents', 'Hour'
        jsonstring= ConnectionClass().JsonFromQuery(query, headers)
        return jsonstring


       