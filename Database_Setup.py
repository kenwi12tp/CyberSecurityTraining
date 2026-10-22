#id	username	role
#1	Admin	administrator
#2	Kewin	user

#Tabel 2: login_events
#id	user_id	ip_address	status
#1	1	192.168.1.10	FAILED
#2	1	192.168.1.10	SUCCESS
#3	2	10.0.0.5	FAILED
import sqlite3
import random as rnd

login_events = []
users = [[1,"Admin", "administrator"], [2,"Kewin", "user"]]
statuses = ["SUCCESS","FAILED"]
ips = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30",
    "192.168.1.40",
    "192.168.1.50",
    "192.168.1.60",
    "192.168.1.70",
    "192.168.1.80",
    "10.0.0.5",
    "10.0.0.10",
    "10.0.0.15",
    "10.0.0.20",
    "172.16.0.10",
    "172.16.0.20",
    "172.16.0.30",
    "172.16.0.40",
    "203.0.113.10",
    "203.0.113.20",
    "198.51.100.15",
    "198.51.100.25"
]
user_ids = [1,2]

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("security.db")

# Create a cursor object
cursor = conn.cursor()

#Create a table - decide on a structure

#cursor.execute("""DROP TABLE users
#""")
# cursor.execute("""
#  CREATE TABLE  users (
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      user_id INTEGER,
#      username TEXT,
#      role TEXT
#  )
#  """)
#
# #Create a table - decide on a structure
# cursor.execute("""
# CREATE TABLE login_events (
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      user_id INTEGER,
#      ip_address TEXT,
#      status TEXT
#  )
#  """)

#for altering tables
#cursor.execute("""ALTER TABLE login_events ADD COLUMN timestamp TEXT""")

for i in range(0, 501):
    login_events.append((rnd.choice(user_ids),rnd.choice(ips),rnd.choice(statuses)))

#creating a bruteforce hacker to the database
for i in range(0, 31):
    if i < 30:
        login_events.append((2,"203.0.113.10","FAILED",))
    else:
        login_events.append((2,"203.0.113.10","FAILED",))
#inserting data via a list
#cursor.executemany("""INSERT INTO login_events (user_id, ip_address, status) VALUES (?, ?, ?)""", login_events)
#cursor.executemany("""INSERT INTO users (user_id, username, role) VALUES (?, ?, ?)""", users)

#deleting data if i need to
#cursor.execute("""DELETE FROM users""")

#saving the data in the database
conn.commit()