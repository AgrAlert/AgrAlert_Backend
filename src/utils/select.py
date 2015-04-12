import sqlite3


conn = sqlite3.connect('agralert.db')
curs = conn.cursor()

curs.execute("SELECT * FROM agr")

print curs.fetchall()

