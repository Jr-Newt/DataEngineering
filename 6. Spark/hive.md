# Hive

> Apache Hive is a SQL-like open source data warehousing application that extracts data from hadoop and related systems.

- Hadoop Ecosystem
- Runs on Hadoop services.
- Hive Query --> Map + Reduce
- Batch Processing
- Suitable for Structured or Semi-Structured

## Hive Architecture

The main components of the hive architecture include Hadoop core components, metastore, driver and hive clients.

![alt text](<img/hive arch.PNG>)

### Hive Job flow
1. Parse HiveQL 
    * Syntax is checked at this stage,Error,Schema and DataType
    * If error is not found it will convert into DAG.

2. Optimizer: It optimizes the query. you can add catalyst for fast execution.

3. Executor: It splits job into multiple tasks and executes the tast. 

    DAG --> MapReduce

4. Submit jobs to cluster
5. Monitor progress
6. Process data in MapReduce or Apache Spark
7. Store Data in HDFS

