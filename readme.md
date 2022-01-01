
## Steps to reproduce

### Prerequisites
1.Install python 3.x and below 2 packages:
   1. psycopg2
   2. requests 
   3. json (if already not installed)

2.PostgreSQL Instance and client tool to connect (like DBeaver)

### Task 1: 
1. Create a database/schema on PostgreSQL instance
2. Create 3 tables ([Check the folder for Scripts: sql/ddl](https://github.com/sanojtomar/data-engineer-spark-networks/tree/master/sql/ddl))
   1. users
   2. subscriptions
   3. messages
3. Clone this repository files to a desired location/server
4. Create a database config file (database.ini) or update existing one with database connection setting:
  
    [postgresql]<br />
    host=HOST_URL_OR_IP_HERE<br />
    database=DATABASE_NAME_HERE<br />
    user=USER_NAME_HERE<br />
    password=ENTER_PASSWORD_HERE<br />

### How to run [Windows]
#### Command: python main.py
1. Manually: Navigate to code directory with command prompt (CMD) and run the command 
2. Schedule: Same command can be scheduled in windows task scheduler

### Task 2: SQL Queries for data analysis
[Check the folder for queries: sql/queries](https://github.com/sanojtomar/data-engineer-spark-networks/tree/master/sql/queries)
    

### Note:
I could have done this task with Azure data factory/data bricks/spark, 
however I have developed the task with Python and SQL only as mentioned in the requirement document.


