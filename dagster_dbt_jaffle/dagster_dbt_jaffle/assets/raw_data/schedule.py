## schedule job to run daily
from dagster import AssetSelection, ScheduleDefinition, define_asset_job

asset_job = define_asset_job("asset_job", AssetSelection.groups("default"))

basic_schedule = ScheduleDefinition(job=asset_job, cron_schedule="0 0 * * *")