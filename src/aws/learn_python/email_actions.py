import smtplib
import logging
from typing import List

from src.aws import config
from src.aws.exceptions import ConfigException

log = logging.getLogger(__name__)

def send_email():

    smtp_host = config.get('smtp', 'SMTP_HOST')
    smtp_port = config.getint('smtp', 'SMTP_PORT')
    smtp_starttls = config.getboolean('smtp', 'SMTP_STARTTLS')
    smtp_ssl = config.getboolean('smtp', 'SMTP_SSL')
    smtp_user = None
    smtp_password = None

    try:
        smtp_user = config.get('smtp', 'SMTP_USER')
        smtp_password = config.get('smtp', 'SMTP_PASSWORD')
    except ConfigException:
        log.error("User/Password was not provided for SMTP connection")

    conn = smtplib.SMTP_SSL(smtp_host, smtp_port) if smtp_ssl else smtplib.SMTP(smtp_host, smtp_port)
    if smtp_starttls:
        conn.starttls()
    if smtp_user and smtp_password:
        conn.login(user=smtp_user, password=smtp_password)
        conn.sendmail("from", "to", "mime")
        conn.quit()

# ??
def get_email_list_from_str(addresses: str) -> List[str]:
    delimiters = [',', ';']
    for delimiter in delimiters:
        if delimiter in addresses:
            return [address.strip() for address in addresses.split(delimiter)]
    return [addresses]


if __name__ == '__main__':
    address = "email1@gmail.com,email2@gmail.com;email3@gmail.com"
    result = get_email_list_from_str(address)
    print(result)
    print(result.__class__.__name__)