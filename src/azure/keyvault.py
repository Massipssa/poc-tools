from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Your Azure Key Vault URL
keyvault_url = "https://<Your-KeyVault-Name>.vault.azure.net"
secret_name = "<Your-Secret-Name>"

# Create a credential object using environment variables, Managed Identity, or a service principal
credential = DefaultAzureCredential()

# Create a SecretClient to interact with Azure Key Vault
client = SecretClient(vault_url=keyvault_url, credential=credential)


# Retrieve the secret's value
retrieved_secret = client.get_secret(secret_name)

# Access the secret's value
secret_value = retrieved_secret.value

print(f"The secret '{secret_name}' has the value: {secret_value}")