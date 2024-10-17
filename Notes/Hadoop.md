# Hadoop
## Installation

```
mkdir

```

# Yarn
### Architecture
![alt text](img/image-3.png)

1. Job Scheduler
    * When user submits Job, it goes to Job scheduler and its schedules Job using FIFO, FAIR and Capaciy Schedulers.

    * Job Scheduler will allocate resources for the job.

2. Application Manager
    * Application Manager will accept the job from job scheduler.
    * It will request node manager to allocate containers (Resources - RAM, CPU, Netwrok, Data Blocks)
    * Application Manager will monitor job execution, if required more resources. It will request to distribute resources as required.
    * If job fails, Application manager will request to restart job.

3. Node Manager
    * Node Manager will allocate resources and App Master to monitor containers.
    * App Master will monitor resources and will negotiate about resources for running job.
    * App Master will kill itself once job is finished.
    * Node manager will send the staus of slave node using signal (heartbeat), signal sent at regular interval.

### MapReduce
> The key reason to perform mapping and reducing is to speed up the execution of a specific process by splitting a process into number of task, thus it encourages parallelism in job flow.

#### Input Split and Record Reader
![alt text](img/image5.png)




