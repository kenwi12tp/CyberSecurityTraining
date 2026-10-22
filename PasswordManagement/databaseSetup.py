import sqlite3
conn = sqlite3.connect("passwordManagementDatabase.db")
cursor = conn.cursor()
cursor.execute("""DROP TABLE users""")
cursor.execute("""
 CREATE TABLE  users (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     username TEXT,
     Password_hash TEXT,
     salt TEXT
 )
 """)
conn.commit()
conn.close()