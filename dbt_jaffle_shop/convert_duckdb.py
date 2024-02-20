import duckdb
print("Converting db duck to new file")
conn = duckdb.connect ('jaffle_shop_db.duckdb') 
conn.execute ("EXPORT DATABASE 'tmp'")
print("After Converting...")
# cursor = duckdb.connect()
# print(cursor.execute('SELECT 42').fetchall())
