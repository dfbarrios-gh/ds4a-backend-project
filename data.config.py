#!/usr/bin/python
from configparser import ConfigParser
 
filePath = 'database.ini'
#filePath = 'database.ini'
def config(file = filePath, section = 'postgresql'):
    
    parser = ConfigParser()
    parser.read(file)
    
    db = {}
    if parser.has_section(section):
        params = parser.items(section)

        for param in params:
            db[param[0]] = param[1]
        
        return db
    else:
        raise Exception('Section {0} did not found {1} into file'.format(section, file))