import hvac
import sys


VAULT_HOST = 'http://127.0.0.1:8200'
VAULT_TOKEN = 'root'
PATH = 'my-secret-password'


if __name__ == '__main__':

    # Authentication
    client = hvac.Client(
        url=VAULT_HOST,
        token=VAULT_TOKEN,
    )
    
    # Writing a secret
    create_response = client.secrets.kv.v2.create_or_update_secret(
        path='my-secret-password',
        secret=dict(password='Hashi123'),
    )

    print('Secret written successfully.')
    

    # Reading a secret
    read_response = client.secrets.kv.v2.read_secret_version(path=PATH)
    print(read_response)

    
    password = read_response['data']['data']['password']

    if password != 'Hashi123':
        sys.exit('unexpected password')

    print(f"Password: {password}")