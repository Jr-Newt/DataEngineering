from azure.cosmos import CosmosClient, PartitionKey, exceptions
import json


# setting up the connectivity

endpoint = "https://azurecosmos-newt-demo1.documents.azure.com:443/"
key = "sGr9RqXNZg0r3aFBG0JYUyS8QffNyLDJ9cWZ3ltKm7JQvH6hDPANaPQbREN7KbgndHdNHPAaZlcPACDbG6qBTg=="
DATABASE_NAME = "customer-AzureDB"
CONTAINER_NAME = "customerContainer"

# Create a Cosmos client - to establish a connection with Azure CosmosDB
client = CosmosClient(endpoint,key)

# select the database
database = client.get_database_client(DATABASE_NAME)

# select container name
container = database.get_container_client(CONTAINER_NAME)


# inputing json
with open('customer.json', 'r') as file:
    customersJson = json.load(file)


try:
    for item in customersJson:
        container.create_item(body=item)
    
except  exceptions.CosmosHttpResponseError as E:
    print(f'Error: ${E.message}')


# print(database)
# print(container)
