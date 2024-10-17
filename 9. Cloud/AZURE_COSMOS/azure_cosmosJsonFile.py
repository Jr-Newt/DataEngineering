from azure.cosmos import CosmosClient, PartitionKey, exceptions
import json


# setting up the connectivity

endpoint = "https://azurecosmos-newt-demo1.documents.azure.com:443/"
key = "sGr9RqXNZg0r3aFBG0JYUyS8QffNyLDJ9cWZ3ltKm7JQvH6hDPANaPQbREN7KbgndHdNHPAaZlcPACDbG6qBTg=="
DATABASE_NAME = "bank-AzureDB"
CONTAINER_NAME = "bankcontainer"

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

    records = []
    count = 0
    for record in items:
        count += 1
        
        records.append(record)
    

    
    with open('bank.json', 'w') as f:
        json.dump(records, f,indent =4)

except exceptions.CosmosHttpResponseError as e:
    print(f"A error occurred: {e.message}")



