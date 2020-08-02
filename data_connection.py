#!/usr/bin/python
import json
import psycopg2
import pandas as pd
from flask import jsonify
from data_config import config
 
class ConnectionClass:

    def JsonFromQuery(self, query, headers):
        connection = None

        try:
            params = config()
            connection = psycopg2.connect(**params)

            cur = connection.cursor()
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
            if connection is not None:
                connection.close()

    def DataframeFromQuery(self, query):
        connection = None

        try:
            params = config()
            connection = psycopg2.connect(**params)
            dataframe = pd.read_sql_query(query, con = connection)
            print(dataframe)
            return dataframe

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if connection is not None:
                connection.close()

    #def JsonListFromQuery(self, query):
    #    connection = None
    #
    #    try:
    #        params = config()
    #        connection = psycopg2.connect(**params)
    #        dataframe = pd.read_sql_query(query, con = connection)
    #        #print(dataframe)
    #
    #        jsonresponse = '{'
    #        for column in dataframe:
    #            columnSerie = dataframe[column]
    #            #print(columnSerie.name)
    #            #print(columnSerie.tolist())
    #            jsonresponse = jsonresponse + ' "' + str(columnSerie.name) + '" : ' + str(columnSerie.tolist()) + ','
    #        jsonresponse = jsonresponse + '}'
    #        #print(jsonresponse)
    #        return jsonresponse
    #
    #    except (Exception, psycopg2.DatabaseError) as error:
    #        print(error)
    #
    #    finally:
    #        if connection is not None:
    #            connection.close()
    #
    ## Iterate over the sequence of column names
