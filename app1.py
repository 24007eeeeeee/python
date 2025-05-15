import sqlite3

db = sqlite3.connect("SWfilms.db")
cursor = db.cursor()
sql = "SELECT * from movie;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()