from data_connection import ConnectionClass

class VehiclesBusiness:

    def GetVehicles(self):
        query = 'SELECT * from vehicles limit 100'
        headers = 'CODIGO_SINIESTRO', 'FECHA', 'VEHICULO', 'CLASE', 'SERVICIO', 'ENFUGA'
        return ConnectionClass().JsonFromQuery(query, headers)