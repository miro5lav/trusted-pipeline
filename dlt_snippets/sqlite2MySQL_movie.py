# get movie table from SQLite and copy it to MySQL database
import dlt
from dlt.common.typing import TDataItems
from dlt.common.schema import TTableSchema
import sqlite3
import mysql.connector
from dlt.common.typing import TDataItems
from dlt.common.schema import TTableSchema

## retrieve data from sqllite
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("SELECT * FROM movie")
movies = cur.fetchall()

## Clean way to declare incremental load with update by year column
@dlt.resource(
    write_disposition="merge",
    primary_key="year",
)
def users():
    yield from movies

# Get mySql connection with hardcoded values
mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='Password', use_pure=True)
mydb.autocommit = True


def get_columns_name():
    return ['title', 'year', 'user_score', 'critic_score']

# you can use decorator here
@dlt.destination(
    batch_size=10,
    max_parallel_load_jobs=1,
)
def my_destination_2(items: TDataItems, table: TTableSchema) -> None:
  DB_NAME = 'test'
  cur = mydb.cursor(dictionary=True)
  cur.execute("USE {}".format(DB_NAME))
  for item in items:
    single_row = ( item['value']) # no eval expression required
    placeholders = ', '.join(['%s'] * len(single_row))
    movie_name = 'movie'
    columns =','.join(i for i in get_columns_name() )
    values = list(single_row)
    print(values )
    sql = f"INSERT INTO {movie_name} ({columns}) VALUES({placeholders})"
    print(sql )
    cur.execute(sql, values)
  #con.commit()
  mydb.close()

# reference function directly, need to change pipeline name if changing number of columns
p = dlt.pipeline("my_mysql_pipe", destination=my_destination_2)

# now run pipeline with custom destination
load_info = p.run(users, table_name="movie")
print(load_info)