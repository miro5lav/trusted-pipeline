This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project).

This is dagster job running simple pipeline in dlt coping issues from Github into Snowflake or DuckDB.

Run with:
**dagster dev**

Remember to have defined credentials in .env file or use dlt credential settings in .dlt/secrets.toml folder.

Once logged into dagster materialize your new pipeline on snowflake/duckdb.

If something is not working use :
dagster dev --help 
to set up --working-directory or other parameters :satisfied: .