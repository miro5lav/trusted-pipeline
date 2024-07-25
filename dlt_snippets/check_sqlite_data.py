# get values from sqllite after executing custome_destination_sqllite.py one destination
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("SELECT * FROM movie")
print("Display all movies:\n", cur.fetchall())
cur.close()
con.commit()
con.close()