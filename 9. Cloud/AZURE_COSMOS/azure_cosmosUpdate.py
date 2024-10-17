from azure.cosmos import CosmosClient, PartitionKey, exceptions
import json


# setting up the connectivity

endpoint = ""
key = "
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

    item = container.read_item(item=recordID, partition_key=partitionKey)
    
    # Modify the item as needed
    item['name'] = 'Issac Wilson'
    item['amount'] = 25000
    item['product'] = 'smartphone'
    item['brand-name'] = 'samsung'

    updated_item = container.replace_item(item=item, body=item)
    print(f"Record with ID {recordID} updated successfully.")
    print(f"Updated item: {json.dumps(updated_item, indent=2)}")
except exceptions.CosmosResourceNotFoundError:
    print(f"Record with ID {recordID} not found.")
except exceptions.CosmosHttpResponseError as e:
    print(f'Error updating record: {e.message}')


# print(database)
# print(container)
