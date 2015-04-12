import sqlite3

db = sqlite3.connect('agralert.db')
db.execute("CREATE TABLE agr (id INTEGER PRIMARY KEY, latitude REAL, longitude REAL, title TEXT)")
db.execute("INSERT INTO agr (latitude,longitude,title) VALUES (45.4,50.23, 'CROP: Citrus, ISSUE: dry root rot')")
db.execute("INSERT INTO agr (latitude,longitude,title) VALUES (50.4,32.1, 'CROP: wheat, ISSUE: Barley stripe')")
db.commit()


