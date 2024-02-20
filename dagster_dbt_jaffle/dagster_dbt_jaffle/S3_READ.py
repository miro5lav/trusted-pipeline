import boto3
import pandas as pd
import sys

#  

if sys.version_info[0] < 3: 
    from StringIO import StringIO # Python 2.x
else:
    from io import StringIO # Python 3.x

client = boto3.client('s3')

bucket_name = 's3://dbt-tutorial-public'

object_key = 'jaffle_shop_orders.csv'
csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')

df = pd.read_csv(StringIO(csv_string))

print(df.columns)