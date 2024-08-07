# Check if data was loaded from API into our own database
import duckdb

con = duckdb.connect(database= 'github_issues.duckdb')
print( con.sql("describe"))

cur = con.cursor()

cur.execute('SELECT  * FROM dagster_github_issues.github_issues limit 1')
results = cur.fetchall()
print( results)
