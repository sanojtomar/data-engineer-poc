
## Steps to reproduce

### Prerequisites
1.Install python 3.x and below 2 packages:
   1. psycopg2
   2. requests
   3. PostgreSQL Instance

### Task 1: 
1. Create a database/schema on PostgreSQL instance
2. Create 3 tables (Scripts are given --> sql/ddl)
   1. users
   2. subscriptions
   3. messages
3. Clone this repository files to a desired location/server
4. Create a database config file (database.ini) or update existing one with database connection setting:
  
    [postgresql]
    host=HOST_URL_OR_IP_HERE
    database=DATABASE_NAME_HERE
    user=USER_NAME_HERE
    password=ENTER_PASSWORD_HERE

#### How to run [Windows]
Command: python main.py
1. Manually: Navigate to code directory with command prompt (CMD) and run the command 
2. Schedule: Same command can be scheduled in windows task scheduler

### Task 2: SQL Queries for data analysis
   Check the folder sql/queries

### Note:
I could have done this task with Azure data factory/data bricks or spark, 
however I wanted to develop the task with Python and SQL only as mentioned in the document.


