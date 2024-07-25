# load test json file to Snowflake database
# dlt_data must have privileges to access them from loader user
import json
import dlt


with open("test.json", 'r') as file:
    data = json.load(file)

pipeline = dlt.pipeline(
	pipeline_name='from_json2snowflake',
	destination='snowflake',
	dataset_name='dlt_data',
  dev_mode=False,
)
# dlt works with lists of dicts, so wrap data to the list
load_info = pipeline.run([data], table_name="sf_data")
print(load_info)