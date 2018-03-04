#!/usr/bin/python
from configparser import ConfigParser
import os

class MissingSection(BaseException):
    """Exception raised for errors when read a section from file.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class MissingInMemoryValues(BaseException):
    """Exception raised for errors while trying load in memory values to parameters.
       Only if config file not found.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def pgConfig(section='postgresql', filename='config.ini'):
    
    # Test if config.ini exists
    if not os.path.exists(filename):
        # get connection params from env vars
        host = os.getenv('HOST', 'localhost')
        port = os.getenv('PORT', 5432)
        database = os.getenv('DBNAME', 'bitcointoyou')
        username = os.getenv('DBUSER', 'postgres')
        password = os.getenv('DBPASS', 'postgres')

        with open(filename, "w") as configfile:
            print("[postgresql]", file=configfile)
            print("host={}".format(host), file=configfile)
            print("port={}".format(port), file=configfile)
            print("database={}".format(database), file=configfile)
            print("user={}".format(username), file=configfile)
            print("password={}".format(password), file=configfile)
        
    return getConfig(section)

def exchangeConfig(section='exchange', filename='config.ini'):
    
    # Test if config.ini exists
    if not os.path.exists(filename):
        # get API params from env vars
        api_key = os.getenv('APIKEY')
        secrete_key = os.getenv('SECRETEKEY')
        if not api_key or secrete_key:
            raise MissingInMemoryValues('Loads keys', 'The Exchange keys are not loaded.')

        with open(filename, "w") as configfile:
            print("["+section+"]", file=configfile)
            print("api_key={}".format(api_key), file=configfile)
            print("secrete_key={}".format(secrete_key), file=configfile)
        
    return getConfig(section)

def getConfig(section, filename='config.ini'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise MissingSection('Get configuration',
            'Section {0} not found in the {1} file'.format(section, filename))
 
    return db