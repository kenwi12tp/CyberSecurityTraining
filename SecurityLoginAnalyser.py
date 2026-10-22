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

#printing it
print(f"========== SECURITY ANALYZER ==========\n\ntotal login attempts:{count_events}"
      f"\ntotal failed attempts:{count_failed}"
      f"\ntotal successfull attempts:{count_success}"
      f"\nprocentage successfull attempts:{round(percentage,2)}%")