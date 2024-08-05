## loads data into postgres table located on Docker Desktop mysql 8.0.38
import datetime
import dlt
from sql_database import sql_database
from dlt.sources.credentials import ConnectionStringCredentials


def load_selected_tables_from_database() -> None:

    # Create a pipeline
    pipeline = dlt.pipeline(
        pipeline_name="dlt_postgre_chinook", destination=dlt.destinations.postgres(destination_name="mydb"), dataset_name="mydb"
    )

    # Credentials for the sample database.
    # Note: It is recommended to configure credentials in `.dlt/secrets.toml` under `sources.sql_database.credentials`
    credentials = ConnectionStringCredentials(
        "mysql://root:a@localhost:3306/Chinook"
    )
    source_sql = sql_database(credentials).with_resources("Album", "Invoice","Faktura")

    source_sql.Invoice.apply_hints(
        incremental=dlt.sources.incremental(
            cursor_path="InvoiceDate",
            initial_value=datetime.datetime(
                2018, 7, 7, 0, 0, 0, 0, tzinfo=datetime.timezone.utc),

        ),
        primary_key="InvoiceId",
    )
    source_sql.Faktura.apply_hints(
        incremental=dlt.sources.incremental(
            cursor_path="InvoiceDate",
            initial_value=datetime.datetime(
                2021, 3, 6, 0, 0, 0, 0, tzinfo=datetime.timezone.utc),
        ),
        primary_key="InvoiceId",
    )

    source_sql.Album.apply_hints(
        write_disposition="merge",
        primary_key="AlbumId",
    )

    info = pipeline.run(source_sql,
                        write_disposition="merge",
                        # refresh="drop_resources",
                        )

    print("==================================")
    print(info)
    print("==================================")
    print(info.load_packages[0])


if __name__ == "__main__":
    load_selected_tables_from_database()
