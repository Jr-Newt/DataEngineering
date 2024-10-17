# Assignment 5

### A. Create a directory /hadoop/hdfs/ in HDFS 
- `hdfs dfs -mkdir /hadoop/hdfs`

![alt text](1.PNG)

### B. Create a temp directory in Hadoop. Run HDFS command to delete “temp” directory.

- `hdfs dfs -mkdir /temp`
- `hdfs dfs -rm /temp`

![alt text](2.PNG)

### C. List all the files/directories for the given HDFS destination path.
- `hdfs dfs -ls /`

![alt text](c.PNG)

### D. Command that will list the directories in /hadoop folder.
- `hdfs dfs -ls /hadoop `

![alt text](d.PNG)


### E. Command to list recursively all files in hadoop directory and all subdirectories in hadoop directory.
- `hdfs dfs -ls -R /hadoop`

![alt text](e.PNG)

### F. List all the directories inside /hadoop/hdfs/ directory which start with 'dir'.
- `hdfs dfs -ls /hadoop/hdfsdir*`

![alt text](f.PNG)

### G. Create a temp.txt file. Copy this file from the local file system to HDFS.
- `touch temp.txt`
- `hdfs dfs -put temp.txt /hadoop/hdfs`

![alt text](g.PNG)

### H. Copy the file from HDFS to the local file system.
- `hdfs dfs -get hadoop/hdfs/temp.txt /.`

![alt text](h.PNG)

### I. Command to copy from local directory with the source being restricted to a local file reference.
- `hdfs dfs -put /temp1.txt /hadoop/hdfs`

![alt text](i.PNG)


### J. Command to copy to a local directory with the source being restricted to a local file reference.
- `hdfs dfs -get /hdoop/hdfs/temp.txt ./home`

![alt text](j.PNG)

### K. Command to move from the local directory source to Hadoop directory.
- `hdfs dfs -moveFromLocal /temp2.txt /hadoop/hdfs`

![alt text](k.PNG)

### L. Delete the directory and any content under it recursively.
- `hdfs dfs -rm -r /hadoop/hdfs`

![alt text](l.PNG)

### M. List the files and show format file sizes in a human-readable fashion.
- `hdfs dfs -du -h /wordcount`

![alt text](m.PNG)

### N. Take a source file and output the file in text format on the terminal.
- `hdfs dfs -cat tmp.txt`

![alt text](n.PNG)

### O. Display the content of the HDFS file test on your /user/hadoop2 directory.
- `hdfs dfs -cat /wordcount/testHP.txt`

![alt text](o.PNG)

### P. Append the content of a local file test1 to an HDFS file test2.
- `hdfs dfs -appendToFile /tmp.txt /wordcount/testHP.txt`

![alt text](p.PNG)

### Q. Show the capacity, free, and used space of the filesystem.
- `hdfs dfs -df`

![alt text](q.PNG)


### R. Show the capacity, free, and used space of the filesystem. Add parameter formats the sizes of files in a human-readable fashion.
- `hdfs dfs -df -h`

![alt text](r.PNG)

### S. Show the amount of space, in bytes, used by the files that match the specified file pattern.
- `hdfs dfs -du -s /wordcount/testHP.txt`

![alt text](s.PNG)

### T. Show the amount of space, in bytes, used by the files that match the specified file pattern. Format the sizes of files in a human-readable fashion.
- `hdfs dfs -du -h /wordcount/testHP.txt`

![alt text](t.PNG)


### U. Check the health of the Hadoop file system.
- `hdfs fsck / `

![alt text](u.PNG)

### V. Command to turn off the safemode of Name Node.
- `hdfs dfsadmin -safemode leave`

![alt text](v.PNG)

### W. HDFS command to format NameNode.
- `hdfs namenode -format`

### X. Create a file named hdfstest.txt and change its number of replications to 3.

- `hdfs dfs -setrep 3 /wordcount/testHP.txt`

![alt text](x.PNG)

### Y. Write command to display the number of replicas for hdfstest.txt file.
- `hdfs dfs -stat %r /wordcount/testHP.txt`

![alt text](y.PNG)

### Z. Write command to display the status of file “hdfstest.txt” like block size, file size in bytes.
- `hdfs dfs -stat /wordcount/testHP.txt`

![alt text](z.PNG)

### AA. Write HDFS command to change file permission from rw-r--r-- to rwxrwxr-x for hdfstest.txt.
- `hdfs dfs -chmod 761 /wordcount/testHP.txt`

![alt text](aa.PNG)

