#id	username	role
#1	Admin	administrator
#2	Kewin	user

#Tabel 2: login_events
#id	user_id	ip_address	status
#1	1	192.168.1.10	FAILED
#2	1	192.168.1.10	SUCCESS
#3	2	10.0.0.5	FAILED
login_events = [[1,"192.168.1.10", "FAILED"], [1,"192.168.1.10", "SUCCESS"],[2,"10.0.0.5", "FAILED"]]
users = [[1,"Admin", "administrator"], [2,"Kewin", "user"]]
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("security.db")

# Create a cursor object
cursor = conn.cursor()

#Create a table - decide on a structure
##DROP TABLE users
#""")
#cursor.execute("""
#CREATE TABLE users (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    user_id INTEGER,
#    username TEXT,
#    role TEXT
#)
#""")

#cursor.execute("""
#CREATE TABLE login_events (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    user_id INTEGER,
#    ip_address TEXT,
#    status TEXT
#)
#""")
#cursor.executemany("""INSERT INTO login_events (user_id, ip_address, status) VALUES (?, ?, ?)""", login_events)
#cursor.executemany("""INSERT INTO users (user_id, username, role) VALUES (?, ?, ?)""", users)
#conn.commit()