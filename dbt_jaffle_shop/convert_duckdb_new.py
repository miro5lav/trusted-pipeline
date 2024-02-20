import duckdb
print("Converting db duck to new file")
conn = duckdb.connect ('jaffle.new.db') 
conn.execute ("IMPORT DATABASE 'tmp'")
print("After Wrting new file...")
# cursor = duckdb.connect()
# print(cursor.execute('SELECT 42').fetchall())
