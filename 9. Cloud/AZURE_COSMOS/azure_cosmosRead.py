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

query = "SELECT * FROM c"
try:

    items = container.query_items(
        query = query,
        enable_cross_partition_query = True    
    )

    count = 0
    for record in items:
        count += 1
        print(record)

    print(count)


except exceptions.CosmosHttpResponseError as e:
    print(f"A error occurred: {e.message}")


# print(database)
# print(container)
