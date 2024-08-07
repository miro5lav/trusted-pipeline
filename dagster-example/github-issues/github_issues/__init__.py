
from dagster import Definitions, load_assets_from_modules, define_asset_job

from .resources import DltResource
from . import assets
# from dlt.destinations import duckdb("dagster_target.duckdb")
all_assets = load_assets_from_modules([assets])
simple_pipeline = define_asset_job(name="duckdb_pipeline", selection= ['issues_pipeline'])

defs = Definitions(
    assets=all_assets,
    jobs=[simple_pipeline],
    resources={
        "pipeline": DltResource(
            pipeline_name = "github_issues",
            dataset_name = "dagster_github_issues",
            destination = "duckdb",
            table_name= "github_issues"
        ),
    }
)