# Load data using connectorx
import connectorx as cx
import dlt
from dlt.sources.credentials import ConnectionStringCredentials
import datetime

# 2 Extra arguments for running load in parallel
def read_sql_x(
    conn_str: ConnectionStringCredentials = dlt.secrets.value,
    query: str = dlt.config.value,
    p_partition_on: str = 'Id',
    p_partition_num: int = 1

):

    yield cx.read_sql(
        conn_str.to_native_representation(),
        query,
        return_type="arrow2",
        protocol="binary",
        partition_on=p_partition_on,
        partition_num=p_partition_num,
    )

@dlt.resource() # primary_key='InvoiceId'
def invoiceline_resource():
    # create invoice resource with merge on InvoiceId as primary key
    invoice = dlt.resource(
        name="InvoiceLineFinal",
        write_disposition="merge", #merge  or append or replace
        primary_key="InvoiceId",
        standalone=True,
    )(read_sql_x)(
        "mysql://root:a@localhost:3306/Chinook",
        "SELECT * FROM InvoiceLine",
        'InvoiceId',
        5
    )
    return invoice

@dlt.resource()
def invoice_resource():
    # create invoice resource with merge on InvoiceId as primary key
    invoice = dlt.resource(
        name="InvoiceFinal",
        write_disposition="merge", #merge  or append or replace
        primary_key="InvoiceId",
        standalone=True,
    )(read_sql_x)(
        "mysql://root:a@localhost:3306/Chinook",
        "SELECT * FROM Invoice",
        'InvoiceId',
        5
    )
    # add incremental on InvoiceDate in invoice table
    # available data types ['text', 'double', 'bool', 'timestamp', 'bigint', 'binary', 'complex', 'decimal', 'wei', 'date', 'time']
    invoice.apply_hints(incremental=dlt.sources.incremental("InvoiceDate") , columns={"InvoiceId": {"data_type": "double", "nullable": False}, "InvoiceDate":  {"data_type": "timestamp", "nullable": False}}
                        )
    return invoice

if __name__ == "__main__":
    pipeline = dlt.pipeline(pipeline_name="dlt_connectorx-mysql" ,destination=dlt.destinations.snowflake)
    invoice = invoiceline_resource()
    invoice_agg = invoice_resource()
    load_info = pipeline.run(invoice)
    print(load_info)
    print(pipeline.last_trace.last_normalize_info)

    # check that stuff was loaded
    row_counts = pipeline.last_trace.last_normalize_info.row_counts
    print(row_counts)
    assert row_counts["invoice_line_final"] == 2240

    # make sure nothing failed
    load_info.raise_on_failed_jobs()

    # load second table that is parent of invoiceline learn how to use 
    load_info2 = pipeline.run(invoice_agg,table_name="InvoiceFinal")
    print(load_info2)
    print(pipeline.last_trace.last_normalize_info)
    row_counts = pipeline.last_trace.last_normalize_info.row_counts
    print(row_counts)

    load_info2.raise_on_failed_jobs()