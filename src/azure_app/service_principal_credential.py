import os

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient

if __name__ == '__main__':

    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    client_id = os.environ.get("AZURE_CLIENT_ID")
    client_secret = os.environ.get("AZURE_CLIENT_SECRET")
    tenant_id = os.environ.get("AZURE_TENANT_ID")

    credentials = ServicePrincipalCredentials(
        client_id=client_id,
        secret=client_secret,
        tenant=tenant_id
    )

    print(credentials)
    client = ResourceManagementClient(credentials, subscription_id)

    print(client.resource_groups.list())
    for item in client.resource_groups.list():
        print(item)

