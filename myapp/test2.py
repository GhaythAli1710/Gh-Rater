import sqlite3

connection = sqlite3.connect("gh.db")
cur = connection.cursor()

# cur.execute("""create table gh
# (
# name text,
# email text,
# age integer
# )""")

# cur.execute('insert into gh values("ghayth","ghayth@gmail.com",25)')

# cur.execute("select * from gh")
# print(cur.fetchone())

connection.commit()
connection.close()
