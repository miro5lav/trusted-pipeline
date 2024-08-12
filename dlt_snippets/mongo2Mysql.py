import dlt
from dlt.common.pipeline import LoadInfo
from dlt.common.schema import TTableSchema
from dlt.common.typing import TDataItems
from dlt.pipeline.pipeline import Pipeline
import mysql.connector

# As this pipeline can be run as standalone script or as part of the tests, we need to handle the import differently.
try:
    from .mongodb import mongodb, mongodb_collection  # type: ignore
except ImportError:
    from mongodb import mongodb, mongodb_collection

# Get mySql connection with hardcoded values
mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='xxx', use_pure=True)
mydb.autocommit = True

# column defined in Mongo db collection '_dlt_load_id','_dlt_id','manager_id__v_text',
def get_columns_name():
    return ['_id', 'employee_id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'job_id','salary','commission_pct','manager_id','department_id' ]

# you can use decorator here
@dlt.destination(
    batch_size=25,
    max_parallel_load_jobs=1,
    name= 'customers2'
)
def my_destination(items: TDataItems, table: TTableSchema) -> None:
  DB_NAME = 'retail'
  cur = mydb.cursor() # dictionary=True
  cur.execute("USE {}".format(DB_NAME))
  print("Getting data into mysql database")
  for item in items:
    placeholders = ', '.join(['%s'] * len(item))
    custom_table_name = 'customers2'
    columns =','.join( i for i in get_columns_name() )
    values = list(item.values())
    #print(values )
    sql = f"INSERT INTO {custom_table_name} ({columns}) VALUES({placeholders})"
    #print(sql )
    cur.execute(sql, values)
  print("Data should be loaded into mysql database")
  mydb.commit()


# end of mysql setup
def load_select_collection_db(pipeline: Pipeline = None) -> LoadInfo:
    """Use the mongodb source to reflect an entire database schema and load select tables from it.
    This example sources data from a sample mongo database data from [mongodb-sample-dataset](https://github.com/neelabalan/mongodb-sample-dataset).
    """
    if pipeline is None:
        # Create a pipeline
        pipeline = dlt.pipeline(
            pipeline_name="local_mysqlmongo",
            destination=my_destination, # custom destination in pipeline
            dataset_name="retail",
        )

    # Configure the source to load a few select collections incrementally incremental=dlt.sources.incremental("EMPLOYEE_ID") does sometimes work
    mflix = mongodb().with_resources(
        "customers"
    )
    #

    # Run the pipeline. The merge write disposition merges existing rows in the destination by primary key , this seems to not work
    info = pipeline.run(mflix,primary_key='employee_id',  write_disposition="merge")

    return info

if __name__ == "__main__":
    # Credentials for the sample database.
    print(load_select_collection_db())
