# try to set up sqllite and duckdb and mysql as destination for loading into sqlite or other database
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, user_score,critic_score)")
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2 ,7.2),
        ('And Now for Something Completely Different', 1971, 7.5, 6)
""")
con.commit()