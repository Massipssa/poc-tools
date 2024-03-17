import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

KEY_VAULT_NAME = "testmkevault" # os.environ['KEY_VAULT_NAME']
SECRET_NAME = "test" #os.environ['SECRET_NAME']

# = os.environ['KEY_VAULT_NAME']
#KEY_VAULT_NAME = os.environ['KEY_VAULT_NAME']
#KEY_VAULT_NAME = os.environ['KEY_VAULT_NAME']


# Your Azure Key Vault URL
keyvault_url = f"https://{KEY_VAULT_NAME}.vault.azure.net"
#secret_name = "<Your-Secret-Name>"

# Create a credential object using environment variables, Managed Identity, or a service principal
credential = DefaultAzureCredential()

# Create a SecretClient to interact with Azure Key Vault
client = SecretClient(vault_url=keyvault_url, credential=credential)


# Retrieve the secret's value
retrieved_secret = client.get_secret(SECRET_NAME)

# Access the secret's value
secret_value = retrieved_secret.value

print(f"The secret '{SECRET_NAME}' has the value: {secret_value}")