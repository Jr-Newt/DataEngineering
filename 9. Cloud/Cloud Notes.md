# Azure

## Azure Storage
Azure storage offers a massive scalablle object store for data objects, a file system for the azure cloud, a messagin store for reliable messaging and a NoSQL store.

**Features:**
- Durable 
- Scalable
- Secure
- Fault - Tolerance
- High Availability
- Managed
- Accessible

**Types of storage are:**
- Blob
- Tables
- Queues
- Files
- Azure import/Export
- AZCopy

##  Blob 
A Massively scalable object sotre for text as well binary data. this is ideal for serving images or documents directly to a browser. Blob stores files for distributed access. Streaming video and audio. Blobs offers backup and restore disaster revoery and archiving.

> PNG, .exe, csv, .txt, .xlxs

#### **Blob storage access tiers:**
 Azure storage provides different option for accessing block of blob data based on usage patterns.
        
- **Hot:** Optimised for frequent access of objects.
- **Cool:** Optimized for storing large amount of data which is infrequently accessible and stored for at 30 days.

- **Archive:** Optmized for data that can tolerate several hours of retrieval latency and it will remain in the archive tier for atleast 180 days. 

## Queue
- A messaging store for reliable messing between application components.

- Its characteristics are: Messaging queue for asynchronous communication between application components.
- This stores an retrives messages in First in First ou(FIFO) order.

- Storage for small pieces of data(source will generate) small messages at regular intervals.

- It is highlt scalable, as this can handle millions of messages per second. This can trigger azure services, functions for automation processing.

> **Usages:**  Processing log message, User Interation with App and background tasks.

## Tables
* Azure storage table is NoSQL key value storage with availablity of the past access and schema-less design
* Usage : Highly scalable and designed for applications requiring large amount of structured,non-relational data. Eg:Logs as key-value pair or metadata.
* This store requires low latency data access and high availablity 


## **Files**
* Managed file share accessible via SMB(Server Message Block) and NFS(Network File System) protocols.Server Message Block protocol is a network file sharing protocol that allows applications on cloud to read and write to files and requesr services from server programs.
- this can also mounted to drives of computers.

### Data Redundancy
* Azure storage that replicates multiple copies of your data.Replication options for a storage include:
    * Local Redundant Storage(LRS)
    * Zone Redundant Storage(ZRS)
    * Geo Redundant Storage(GRS)