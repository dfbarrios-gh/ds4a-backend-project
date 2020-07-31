#!/usr/bin/python
from configparser import ConfigParser
 
def config(file = 'database.ini', section = 'postgresql'):
    parser = ConfigParser()
    parser.read(file)
    
    #print('hello')
    db = {}
    if parser.has_section(section):
        #print('hello agai')
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
        #print(db)
        return db
    else:
        raise Exception('Section {0} did not found {1} into file'.format(section, file))