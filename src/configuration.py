import logging
import os

try:
    import ConfigParser as cp
except ImportError:
    import configparser as cp

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '/learn-python/conf/app.cfg')
    
    
# Init ConfigParser and load --> externalize path 
config = cp.ConfigParser()
config.read(filename)


def database_config():
    url = config.get('database', 'url')
    username = config.get('database', 'username')
    password = config.get('database', 'password')
    
    print(url, " ", username, " ", password)


def get_kerberos() -> None:
    pass


"""
if __name__ == "__main__":
    print(__name__)
    database_config()
"""
