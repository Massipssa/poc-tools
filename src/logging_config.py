"""
- Debug: detailed info
- Info: confirmation that things are working as expected
- Warning
- Error
- Critical
"""

import logging

from src.configuration import conf

logging_level = conf.get("logging", "logging_level")
logging_file = conf.get("logging", "logging_file")
log_format = conf.get("logging", "log_format")

print(logging_level, logging_file, log_format)

logging.basicConfig(filename=logging_file,
                    level=logging_level,
                    format=log_format)


log = logging.getLogger(__name__)

log.info("Hello log")

