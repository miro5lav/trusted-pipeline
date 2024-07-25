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
Comming soon...



# Testing scripts order 
First run scripts that create json database files :

[SQL Lite DB ](create_sqlite_db.py)

[Check SQL Lite DB ](check_sqlite_data.py)

[Insert into SQL Lite DB ](custome_destination_sqllite.py)

Configure and run your local MySQL machine 

[From SQL Lite insert into MySQL db](sqlite2MySQL_movie.py)

[Set Snowflake env variables if secrets.toml file will not work](set_snowflake_envs.py)

Create test.json file in current directory

[Copy json data into your trial versio of Snowflake](json2snowflake.py)