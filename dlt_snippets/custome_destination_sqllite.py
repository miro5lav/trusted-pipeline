# Trying to run clean insert into sqllite
import dlt
import sqlite3
from dlt.common.typing import TDataItems
from dlt.common.schema import TTableSchema

def get_columns_name():
    # cursor =  con.cursor()
    # cursor.execute("SELECT * FROM movie")
    # columns =','.join(i for i in [x[0] for x in cursor.description] )
    # cursor.close()
    return ['title', 'year', 'user_score', 'critic_score']

# use decorator with function
@dlt.destination(
    batch_size=10,
)
def my_destination_2(items: TDataItems, table: TTableSchema) -> None:
  con = sqlite3.connect("tutorial.db")
  cur = con.cursor()
  for item in items:
    single_row = ( item['value']) # no eval expression required
    print( len(single_row), single_row)
    placeholders = ', '.join(['?'] * len(single_row))
    movie_name = 'movie'
    columns =','.join(i for i in get_columns_name() )
    print(columns)
    year = single_row[1]
    cur.execute(f"INSERT INTO {movie_name} ({columns}) VALUES({placeholders})", tuple(single_row) )
  con.commit()
  con.close()

# after defining detination as insert into sqlite create some new data
data4 = [
    ("Scary Movie 3", 1983, 9, 8.2),
    ("Monty Python's Life of Brian", 1979, 8.0 ,9.9),
    ("Ellen ", 1985, 9, 7.3),
]

# reference function directly, need to change pipeline name if changing number of columns
p = dlt.pipeline("my_sqllite_pipe", destination=my_destination_2)

# now run pipeline with custom destination
load_info = p.run(data4 , table_name="movie")
print(load_info)