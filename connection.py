#!/usr/bin/python
import psycopg2
import json
from flask import jsonify
from config import config
 
class ConnectionClass:

    def conectar(self):
        """ Conexión al servidor de pases de datos PostgreSQL """
        conexion = None
        try:
            # Lectura de los parámetros de conexion
            params = config()
            print(params)
            # Conexion al servidor de PostgreSQL
            print('Conectando a la base de datos PostgreSQL...')
            conexion = psycopg2.connect(**params)
    
            # creación del cursor
            cur = conexion.cursor()
            
            # Ejecución de una consulta con la version de PostgreSQL
            print('La version de PostgreSQL es la:')
            cur.execute('SELECT * from accidents limit 10')
    
            columns = ('CODIGO_SINIESTRO', 'FECHA', 'HORA', 'GRAVEDAD', 'CLASE', 'CHOQUE_CON','OBJETO_FIJO', 'DIRECCION', 'TOTAL_MUERTOS', 'TOTAL_HERIDOS', 'LOCALIDAD', 'DISENO_LUGAR')
            results = []
            for row in cur.fetchall():
                 results.append(dict(zip(columns, row)))
            
            #version1 = json.dumps(results, indent = 2)
            version = jsonify(results)

            # Ahora mostramos la version
            #version = cur.fetchone()        
            # Cierre de la comunicación con PostgreSQL
            cur.close()
            return version
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conexion is not None:
                conexion.close()
                print('Conexión finalizada.')
      
#if __name__ == '__main__':
#    conectar()