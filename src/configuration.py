import logging
import os
from typing import Dict, Optional, Union

try:
    import ConfigParser as cp
except ImportError:
    import configparser as cp

log = logging.getLogger(__name__)
# TODO: config logging
logging.basicConfig(filename='myapp.log', level=logging.INFO)

current_path = os.path.abspath(os.path.dirname(__file__))
# TODO: Use Argparser to load config path from cmd
filename = os.path.join(current_path, "../conf/app.cfg")

# Init ConfigParser and load --> externalize path 
conf = cp.ConfigParser()
conf.read(filename)


def database_config():
    url = conf.get('database', 'db_url')
    username = conf.get('database', 'username')
    password = conf.get('database', 'password')

    if log.level == logging.DEBUG:
        log.debug(f"URL {url}, Username {username}, Password: {password}")

    return url, username, password


def get_section(section: str) -> Optional[Dict[str, Union[str, int, float, bool]]]:
    pass


def get_kerberos() -> None:
    pass


class ConfigParser:
    pass


"""
Implement the ConfigParser to adapt our need
"""


class MyConfig(ConfigParser):

    def read(self, filenames, encoding=None):
        super().read(filenames=filenames, encoding=encoding)
