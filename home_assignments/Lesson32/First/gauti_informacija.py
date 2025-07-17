import sqlite3

# Connect to the existing database
conn = sqlite3.connect('knygos.db')
cursor = conn.cursor()

# Fetch all rows from the correct table
cursor.execute("SELECT * FROM knygos")
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

conn.close()

# This script retrieves and prints all book records from the 'knygos' table in the SQLite database 'knygos.db'.
