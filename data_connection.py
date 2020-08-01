#!/usr/bin/python
import json
import psycopg2

from flask import jsonify
from data_config import config
 
class ConnectionClass:

    def JsonFromQuery(self, query, headers):
        conexion = None

        try:
            params = config()
            conexion = psycopg2.connect(**params)

            cur = conexion.cursor()
            cur.execute(query)    
            columns = (headers)
            
            results = []
            for row in cur.fetchall():
                results.append(dict(zip(columns, row)))
            
            jsonResponse = jsonify(results)
            cur.close()
            
            return jsonResponse

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conexion is not None:
                conexion.close()