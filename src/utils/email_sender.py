import collections.abc
import logging
import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from typing import Iterable, List, Union

from src.configuration import conf
from src.exceptions import ConfigException

log = logging.getLogger(__name__)


def send_smtp_email(from_email, to_email, msg):

    smtp_host = conf.get('smtp', 'SMTP_HOST')
    smtp_port = conf.getint('smtp', 'SMTP_PORT')
    smtp_starttls = conf.getboolean('smtp', 'SMTP_STARTTLS')
    smtp_ssl = conf.getboolean('smtp', 'SMTP_SSL')
    smtp_user = None
    smtp_password = None

    try:
        smtp_user = conf.get('smtp', 'SMTP_USER')
        smtp_password = conf.get('smtp', 'SMTP_PASSWORD')
    except ConfigException:
        log.error("User/Password was not provided for SMTP connection")

    conn = smtplib.SMTP_SSL(smtp_host, smtp_port) if smtp_ssl else smtplib.SMTP(smtp_host, smtp_port)
    if smtp_starttls:
        conn.starttls()
    if smtp_user and smtp_password:
        conn.login(user=smtp_user, password=smtp_password)
        conn.sendmail(from_email, to_email, msg.as_string())
        conn.quit()


def get_email_details():
    to = conf.get('email', 'TO')
    cc = conf.getint('email', 'CC')
    subject = conf.getboolean('email', 'SUBJECT')

    to_list = get_email_address_list(to)
    to_comma_separated = ", ".join(to_list)

    if cc is not None:
        cc_list = get_email_address_list(cc)
        cc_comma_separated = ", ".join(cc_list)

    return to, subject, to_comma_separated, cc_comma_separated


def send_email(body, file_name):

    mail_to = conf.get('email', 'FROM')
    mail_from = conf.get('email', 'TO')
    cc = conf.get('email', 'CC')
    subject = conf.get('email', 'SUBJECT')

    msg, recipients = build_msg_attach_file(mail_to, subject, mail_from, cc, body, file_name)
    send_smtp_email(mail_from, mail_to, msg)


def build_msg_attach_file(to, subject, mail_from, cc, body, file_name):

    msg = MIMEMultipart()
    msg['To'] = to
    msg['Subject'] = subject
    msg['From'] = mail_from
    # recipients = ", ".join(to)
    recipients = to

    if cc is not None:
        msg['CC'] = cc # ", ".join(cc)
        recipients = recipients + cc
    msg['Date'] = formatdate(localtime=True)
    msg.attach(MIMEText(body))

    basename = os.path.basename(file_name)
    with open(file_name, "rb") as file:
        part = MIMEApplication(
            file.read(),
            Name=basename
        )
        part['Content-Disposition'] = f'attachment; filename="{basename}"'
        part['Content-ID'] = f'<{basename}>'
        msg.attach(part)

    return msg, recipients


def get_email_address_list(addresses: Union[str, Iterable[str]]) -> List[str]:
    """
    Get list of email address from a str or list of str
    :param addresses:
    :return:
    """
    if isinstance(addresses, str):
        return get_email_list_from_str(addresses)
    elif isinstance(addresses, collections.abc.Iterable):
        if not all(isinstance(item, str) for item in addresses):
            raise TypeError("All emails address must be of string type")
        else:
            return list(addresses)


def get_email_list_from_str(addresses: str) -> List[str]:
    delimiters = [',', ';']
    for delimiter in delimiters:
        if delimiter in addresses:
            return [address.strip() for address in addresses.split(delimiter)]
    return [addresses]


if __name__ == '__main__':

    file_name = "E:/DEV/dev-python/learn-python/conf/result.xlsx"
    body = "Hello, \n Please find attached file ..."

    send_email(body, file_name)
