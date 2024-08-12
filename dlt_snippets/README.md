# *Setting up MySQL*

Download MySQL Community version from https://dev.mysql.com/downloads/mysql/
In My case I am testing old version 8.0.39.

Setup your copied version and in powershell from mysql-8.0.39\bin folder run

.\mysqld.exe --initialize 
This will create data folder within mysql-8.0.39 where you have your default database

.\mysqld.exe --console
This starts your database with default values as localhost:3036

# *Change password in MySQL*
If you do not know root password you can set it up with new one.

Create file mysql-init.txt and Run 

.\mysqld.exe --init-file=C:\\mysql-8.0.39\\bin\\mysql-init.txt --console
This will change your password.
Stop server and run it again!

# *Setting up Snowflake*

You can create free trial on https://signup.snowflake.com/

After connecting to database you set up space for dlt loader :

--create database with standard settings

CREATE DATABASE dlt_data;

-- create new user - set your password here

CREATE USER loader WITH PASSWORD='<password>';

-- we assign all permission to a role

CREATE ROLE DLT_LOADER_ROLE;

GRANT ROLE DLT_LOADER_ROLE TO USER loader;

-- give database access to new role

GRANT USAGE ON DATABASE dlt_data TO DLT_LOADER_ROLE;

-- allow `dlt` to create new schemas

GRANT CREATE SCHEMA ON DATABASE dlt_data TO ROLE DLT_LOADER_ROLE;

-- allow access to a warehouse named COMPUTE_WH

GRANT USAGE ON WAREHOUSE COMPUTE_WH TO DLT_LOADER_ROLE;

-- grant access to all future schemas and tables in the database

GRANT ALL PRIVILEGES ON FUTURE SCHEMAS IN DATABASE dlt_data TO DLT_LOADER_ROLE;

GRANT ALL PRIVILEGES ON FUTURE TABLES IN DATABASE dlt_data TO DLT_LOADER_ROLE;


# Setting up PostgreSQL

MySQL can be installed from bitnami/mysql:8.0.38 image.
PostgreSQL is located in Dockerfiles.



# Testing scripts order 
First run scripts that create json database files :

[SQL Lite DB ](create_sqlite_db.py)

[Check SQL Lite DB ](check_sqlite_data.py)

[Insert into SQL Lite DB ](custome_destination_sqllite.py)

Configure and run your local MySQL machine 

[From SQL Lite insert into MySQL db](sqlite2MySQL_movie.py)

[Set Snowflake env variables if secrets.toml file will not work](set_snowflake_envs.py)

Create test.json file in current directory

[Copy json data into your trial version of Snowflake](json2snowflake.py)

[Create Duck DB for testing](create_duck_db.py)

Link how to copy MySQL data into Snowflake
https://dlthub.com/docs/pipelines/sql_database_mysql/load-data-with-python-from-sql_database_mysql-to-snowflake

# Mongo DB:

Authenticate first user :

mongosh -u "root" -p "xxx" --authenticationDatabase "admin"

Load data into mongoDB as cmd:

mongoimport -u importer --db root --collection customers --type csv --headerline --file employees.csv

or use MondgoDB Compass 
## Check if we have data loaded 
db.customers.find().pretty()

# In Terminal of mongodb you need to create user with 

mongosh

use admin

db.createUser({
  user: "importer",
  pwd: "Pass",
  roles: [
    { role: "readWrite", db: "myDatabase" }
  ]
})

In order to load data from Mongo into MySQL new table must be created on MySQL:

### New table to test loading data from MongoDB to MySQL with dlt

<code>
CREATE TABLE IF NOT EXISTS retail.customers (
    _id VARCHAR(24) PRIMARY KEY,
    EMPLOYEE_ID INT,
    FIRST_NAME VARCHAR(50),
    LAST_NAME VARCHAR(50),
    EMAIL VARCHAR(50),
    PHONE_NUMBER VARCHAR(20),
    HIRE_DATE VARCHAR(20),
    JOB_ID VARCHAR(10),
    SALARY DECIMAL(10, 2),
    COMMISSION_PCT VARCHAR(10),
    MANAGER_ID INT,
    DEPARTMENT_ID INT
);
</code>

Custom destination does not handle data type so Hire date is varchar.

[Script to run](mongo2Mysql.py)

