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


recordID = 'ust10007'
partitionKey = 'India'
try:
    container.delete_item(item=recordID, partition_key=partitionKey)
    print(f"Record with ID {recordID} deleted successfully.")
except exceptions.CosmosResourceNotFoundError:
    print(f"Record with ID {recordID} not found.")
except exceptions.CosmosHttpResponseError as e:
    print(f'Error deleting record: {e.message}')


# print(database)
# print(container)
