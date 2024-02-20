# trusted-data-pipeline

This project is used as a demo for my talk: [Building 3D Trusted Data Pipelines With Dagster, Dbt, and Duckdb](https://2023.pycon.org.au/program/RY9ZCY/) at PyCon Australia 2023

The slides for the workshop is on [this link](https://github.com/danhphan/trusted-data-pipeline/blob/main/assets/slides/Building_3D_Trusted_Data_Pipelines_Aug_2023.pdf).

*Data pipelines and architecture*

<center><img src="./assets/image/3D_data_pipeline.png"/></center>


*Dagster global assets*

<center><img src="./assets/image/dagster_assets.png"/></center>

### Setup Python environment

```
git clone git@github.com:danhphan/trusted-data-pipeline.git
cd trusted-data-pipeline
python3 -m venv venv
source venv/bin/activate
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Setup Dagster

```
cd ./dagster_dbt_jaffle/
dagster dev # or: dagit
```l

### Setup Dbt

```
cd ./dbt_jaffle_shop/
dbt deps
dbt build
```

### Run and test Dbt models

```
dbt run
dbt test
dbt test --select customers
```

### Generate and view docs

```
dbt docs generate
dbt docs serve --port 8081

dbt show --inline "select count(*) from {{ ref('stg_customers') }}"
```

### Problems with config db duck:
Need to install dagster correctly
Need to install db sucks\db correctly. 

Runtime Error
  IO Error: Trying to read a database file with version number 51, but we can only read version 64.
  The database file was created with DuckDB version v0.8.0 or v0.8.1.

  The storage of DuckDB is not yet stable; newer versions of DuckDB cannot read old database files and vice versa.
  The storage will be stabilized when version 1.0 releases.

  For now, we recommend that you load the database file in a supported version of DuckDB, and use the EXPORT DATABASE command followed by IMPORT DATABASE on the current version of DuckDB.

  See the storage page for more information: https://duckdb.org/internals/storage

pip install duckdb==0.10.0
pip install duckdb==0.8.0
$ /older/version/duckdb mydata.db -c "EXPORT DATABASE 'tmp'"
$ /newer/duckdb mydata.new.db -c "IMPORT DATABASE 'tmp'"

0.10.0

Other Data Stack:
https://medium.com/gooddata-developers/how-to-build-a-modern-data-pipeline-cfdd9d14fbea

Read chunks of data:
With duck db:
https://stackoverflow.com/questions/74152013/importing-parquet-file-in-chunks-and-insert-in-duckdb


How to bulk load list values into DuckDB:
https://stackoverflow.com/questions/72945218/how-to-bulk-load-list-values-into-duckdb 



### Dagster tutorial  aftre clone and created jaffle shop ###


dagster-dbt project scaffold --project-name jaffle_dagster

## sprawdz jutor czy dziala projekt !!!
FileExistsError: [WinError 183] Nie można utworzyć pliku, który już istnieje: 'C:\\Users\\mr186\\Documents\\LocalRepo\\trusted-3d-pipeline\\tutorial-dbt-dagster\\jaffle_shop\\jaffle_dagster'

## run dagster in powershell
$env:DAGSTER_DBT_PARSE_PROJECT_ON_LOAD = "1"; dagster dev

                                                                                                                                                                                                                                                                                
 cd 'C:\Users\mr186\Documents\LocalRepo\trusted-3d-pipeline\tutorial-dbt-dagster\jaffle_shop' \
   && dbt parse --target-path target \
   && cd 'C:\Users\mr186\Documents\LocalRepo\trusted-3d-pipeline\tutorial-dbt-dagster\jaffle_shop\jaffle_dagster' \
   && dagster dev
   dbt parse --