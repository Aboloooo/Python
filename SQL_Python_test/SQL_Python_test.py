import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS class(id, name, number)")
cur.execute("INSERT INTO class VALUES (1, 'Lily', 1)")
cur.execute("INSERT INTO class VALUES (2, 'Lily', 2)")

con.commit()

res = cur.execute("SELECT * FROM class")


# print(res.fetchall())
for row in cur.execute("SELECT name FROM class"):
    print(row)