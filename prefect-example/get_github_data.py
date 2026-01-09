# Check if data was loaded from API into our own duck database
import duckdb

con = duckdb.connect(database= 'github_dynamic_issues.duckdb')
print( con.sql("describe"))

con3 = duckdb.connect(database= 'github_dynamic_releases.duckdb')
print( con3.sql("describe"))

con2 = duckdb.connect(database= 'github_dynamic_repos.duckdb')
print( con2.sql("describe"))

con4 = duckdb.connect(database= 'github_dynamic_contributors.duckdb')
print( con4.sql("describe"))
# cur = con.cursor()

# cur.execute('SELECT  * FROM github_data.issues limit 1')
# results = cur.fetchall()
# print("Issue example", results)

# cur.execute('SELECT  * FROM github_data.repos limit 1')
# results = cur.fetchall()
# print("Repo example", results)