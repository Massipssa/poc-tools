import logging
import os
from pathlib import Path


try:
    import ConfigParser as cp
except ImportError:
    import configparser as cp

filename = "../conf/app.cfg"

# Init ConfigParser and load --> externalize path 
config = cp.ConfigParser()
config.read(filename)


def database_config():
    url = config.get('database', 'db_url')
    username = config.get('database', 'username')
    password = config.get('database', 'password')
    
    print(url, " ", username, " ", password)


def get_kerberos() -> None:
    pass


