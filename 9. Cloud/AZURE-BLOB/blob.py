from azure.storage.blob import ContainerClient, BlobClient, BlobServiceClient

#connection String
connectionString = "BLOB_CONNECTION_STRING"
accountKey = "BLOB_ACCOUNT_KEY"
accountName = "BLOB_ACCOUNT_NAME"

blobStorageClient = BlobServiceClient.from_connection_string(connectionString)
print(blobStorageClient)

blobClient = BlobServiceClient(account_url = f"https://{accountName}.blob.core.windows.net/",
                  credential = accountKey)

#Access Container and List Blobs
containerName = "azureblobcontainer"
containerClient = blobStorageClient.get_container_client(containerName)
#List all blobs

# blobList = containerClient.list_blob_names()
# for blobs in blobList:
#     print(blobs)


# Create a container if it doesn't exists
def create_container(containerName):
    containerClient = blobStorageClient.get_container_client(containerName)
    try:
        containerClient.create_container()
        print(f"Container {containerName} created")
    except Exception as e:
        print(f"Container creation failed {e}")

def upload_blob(container_Name, blob_name, data):
    blob_client = blobClient.get_blob_client(container=container_Name,
                                             blob=blob_name)
    try:
        blob_client.upload_blob(data=data, overwrite=True)
        print("Uploaded")
    except Exception as e:
        print(f"blob upload failed with {e}")

def delete_blob(container_Name, blob_name):
    blob_client = blobClient.get_blob_client(container=container_Name,
                                             blob=blob_name)
    try:
        blob_client.delete_blob()
        print(f"BLOB {blob_name} DELETED")
    except Exception as e:
        print(f"Blob Deletion failerd {e}")

def download_blob(container_Name, blob_name, download_file_path):
    blob_client = blobClient.get_blob_client(container=container_Name,
                                             blob=blob_name)
    
    try:
        with open(download_file_path, "wb") as fileobj:
            fileobj.write(blob_client.download_blob().readall())
            print("Downloaded")
    except Exception as e:
        print(f"Download ERROR {e}")

if __name__ == "__main__":
    # create_container("azuredemocontainer")

    #upload (create) a blob
    # upload_blob("azuredemocontainer", "blobfile.txt", "https://youtu.be/dQw4w9WgXcQ?si=TCzwz5HpeNLkylqL")

    # delete_blob("azuredemocontainer","blobfile2.txt")


    download_blob("azuredemocontainer", "blobfile.txt", "mamooty.jpg")


