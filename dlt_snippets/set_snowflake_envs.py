# This are setting for pipeline name FROM_JSON2SNOWFLAKE for setting environment variables for snowflake connection if you don't want to store them in secrets.toml 
import os
os.environ.setdefault('FROM_JSON2SNOWFLAKE__DESTINATION__SNOWFLAKE__CREDENTIALS__DATABASE','dlt_data')
os.environ.setdefault('FROM_JSON2SNOWFLAKE__DESTINATION__SNOWFLAKE__CREDENTIALS__USERNAME','loader')
os.environ.setdefault('FROM_JSON2SNOWFLAKE__DESTINATION__SNOWFLAKE__CREDENTIALS__HOST','ggxxxxxx-xx17667')
os.environ.setdefault('FROM_JSON2SNOWFLAKE__DESTINATION__SNOWFLAKE__CREDENTIALS__PASSWORD','Password')
os.environ.setdefault('FROM_JSON2SNOWFLAKE__DESTINATION__SNOWFLAKE__CREDENTIALS__ROLE','DLT_LOADER_ROLE')
os.environ.setdefault('FROM_JSON2SNOWFLAKE__DESTINATION__SNOWFLAKE__CREDENTIALS__WAREHOUSE','COMPUTE_WH')