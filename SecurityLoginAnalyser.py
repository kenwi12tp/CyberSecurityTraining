import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("security.db")

# Create a cursor object
cursor = conn.cursor()

#finding total amount of events
total_events = cursor.execute("SELECT COUNT(*) FROM login_events")
count_events = total_events.fetchone()[0]

#total amounts of failed logins
total_failed = cursor.execute("SELECT COUNT(status) FROM login_events WHERE status = 'FAILED'")
count_failed = total_failed.fetchone()[0]

#total amount of successfull logins
total_success = cursor.execute("SELECT COUNT(status) FROM login_events WHERE status = 'SUCCESS'")
count_success = total_success.fetchone()[0]

#finding the percantage of successfull login attempts
percentage= count_success/count_events*100

cursor.execute("""SELECT ip_address,SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END),SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) 
                  FROM login_events 
                  GROUP BY ip_address 
                  HAVING SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) >= 15 AND SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) >= 1 
                  ORDER BY COUNT(*) DESC""")
potential_bruteforcer = cursor.fetchall()
print(potential_bruteforcer)
#printing it
print(f"========== SECURITY ANALYZER ==========\n"
      f"\ntotal login attempts:{count_events}"
      f"\ntotal failed attempts:{count_failed}"
      f"\ntotal successfull attempts:{count_success}"
      f"\nprocentage successfull attempts:{round(percentage,2)}%"
      f"\n\n========== SECURITY THREATS ==========")
for bruteforcer in potential_bruteforcer:
    print(f"ip address:{bruteforcer[0]} amount of failed login attempts:{bruteforcer[1]} amount of successful login attempts:{bruteforcer[2]}")
cursor.execute("""SELECT users.username, COUNT(*), SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END)
FROM login_events
JOIN users
ON login_events.user_id = users.id
GROUP BY users.username;""")
users = cursor.fetchall()
for user in users:
    user_procent = user[2]/user[1]*100
    print(f"user:{user[0]} has a {round(user_procent,2)}% login success rate")

conn.close()

