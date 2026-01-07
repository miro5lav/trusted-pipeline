# Check if data was loaded from API into our own duck database
import duckdb

con = duckdb.connect(database= 'github_repos_issues.duckdb')
print( con.sql("describe"))

cur = con.cursor()

cur.execute('SELECT  * FROM github_data.issues limit 1')
results = cur.fetchall()
print("Issue example", results)

cur.execute('SELECT  * FROM github_data.repos limit 1')
results = cur.fetchall()
print("Repo example", results)