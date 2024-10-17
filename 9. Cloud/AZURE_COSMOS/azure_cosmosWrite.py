from azure.cosmos import CosmosClient, PartitionKey, exceptions
import json


# setting up the connectivity

endpoint = ""
key = ""
DATABASE_NAME = ""
CONTAINER_NAME = ""

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
