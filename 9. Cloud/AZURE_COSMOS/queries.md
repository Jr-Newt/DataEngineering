### 1. Show all documents from one container.

> select * from c

- c is an alias for the document withtin a container

### 2.  Filtering Documetns based on a field

> SELECT * FROM c WHERE c.balance > 7000

### 3. Limit -Show top 10 records

> select Top 10 * from c

### 4. Aggregate Operations
> select value count(1) from c

### 5. Count with Alias
> select count(1) as count_doc from c

### 6. Sum
> select value sum(c.balance) from c

### 7. AVG
> select value avg(c.balance) from c

### 8. GROUP BY
> select c.job, count(1) as employeeCount, avg(c.balance) as avgBalance
from c GROUP BY c.job

### 9. Order By
> select * from c order by c.balance

### 10. Distinct
> select distinct c.job from c


