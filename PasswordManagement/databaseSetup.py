import sqlite3
conn = sqlite3.connect("passwordManagementDatabase.db")
cursor = conn.cursor()
#cursor.execute("""DROP TABLE users""")
# cursor.execute("""
#  CREATE TABLE  users (
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      username TEXT,
#      role TEXT,
#      Password_hash TEXT
#  )
#  """)
conn.commit()
conn.close()