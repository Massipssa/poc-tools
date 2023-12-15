import logging

from cryptography.fernet import Fernet


log = logging.getLogger(__name__)

global fernet


def read_fernet_key():
    try:
        if fernet is not None:
            return fernet
        else:
            key = config.read('security', 'FERNET_KEY')
            if not key:
                log.warning("Empty key")
    except Exception as e:
        log.error("error")
        raise


def generate_fernet_object(key):
    fernet = Fernet(key)
    return fernet


def generate_key():
    # generate encryption key
    key = Fernet.generate_key()
    print("Key", key)
    return key


def encrypt_value(value):
    # encrypt
    if value is not None:
        token = fernet.encrypt(b"my message")
        print("Value:", token)
    else:
        print("Error value is None")


def decrypt_value(token):
    # decrypt
    if token is not None:
        fernet.decrypt(token)
        print("Value: ", fernet.decrypt(token))

# extract ttl
#print("TTL: ", fernet.extract_timestamp(token))
