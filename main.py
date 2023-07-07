import sqlite3 as sql

with sql.connect("database.db") as con:
    cur = con.cursor()

    cur.execute('SELECT name, score FROM players WHERE score > 70 ORDER BY score DESC')
    for result in cur:
        print(result)
