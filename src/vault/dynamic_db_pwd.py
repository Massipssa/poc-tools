import hvac
import requests


VAULT_HOST = 'http://127.0.0.1:8200'
VAULT_TOKEN = 'root'
PATH = 'database/creds/test-role'


def read_dynamic_pwd_request(): 
    """Read dynamic database password using get request"""
    response = requests.get(
        f'{VAULT_HOST}/v1/{PATH}',
        params={'q': 'requests+language:python'},
        headers={'X-Vault-Token': VAULT_TOKEN},
    )
    if response:
        json_response = response.json()
        print(json_response)
        user = json_response['data']['username']
        password = json_response['data']['password']
        print(f"User: {user}, Password:  {password}")


def read_dynamic_pwd_with_hvac(): 
    """Read dynamic database password using vault python client"""
    client = hvac.Client(
        url=VAULT_HOST,
        token=VAULT_TOKEN,
    )
    response = client.read(PATH)
    if response and 'data' in response:
        secret_data = response['data']
        user = secret_data['username']
        password = secret_data['password']
        print(f"User: {user}, Password:  {password}")


if __name__ == '__main__':

    read_dynamic_pwd_request()
    read_dynamic_pwd_with_hvac()
