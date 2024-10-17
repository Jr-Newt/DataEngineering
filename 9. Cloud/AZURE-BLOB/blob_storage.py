from azure.storage.blob import ContainerClient, BlobClient, BlobServiceClient
from dotenv import load_dotenv, dotenv_values 
import os

load_dotenv()

#connection String
connectionString = os.getenv("BLOB_CONNECTION_STRING")
accountKey = os.getenv("BLOB_ACCOUNT_KEY")
accountName = os.getenv("BLOB_ACCOUNT_NAME")

blobStorageClient = BlobServiceClient.from_connection_string(connectionString)
print(blobStorageClient)

blobClient = BlobServiceClient(account_url = f"https://{accountName}.blob.core.windows.net/",
                  credential = accountKey)

#Access Container and List Blobs
containerName = "azureblobcontainer"
containerClient = blobStorageClient.get_container_client(containerName)

# local_file_path = "transformed_sales_data.json"
# with open(local_file_path, "rb") as fileobj:
#     containerClient.upload_blob("Sales_data.json", fileobj)
#     print(f"Blob Uploaded")

# list all blobs

blobList = containerClient.list_blob_names()
for blobs in blobList:
    print(blobs)
