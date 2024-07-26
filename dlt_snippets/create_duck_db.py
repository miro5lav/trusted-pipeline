import duckdb
import numpy as np
# Create a DuckDB connection and cursor
con = duckdb.connect(database='my_users.duckdb')
cur = con.cursor()

# Create a table
cur.execute('CREATE TABLE users (name VARCHAR, age INTEGER)')

# Insert data into the table
cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))
cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Charlie', 22))

# Commit the changes
con.commit()
# Write the database to a file
cur.sql('SELECT * FROM users').write_csv("users.csv")
con.close()

# Print a success message
print("Data inserted into DuckDB and saved as users.csv")
