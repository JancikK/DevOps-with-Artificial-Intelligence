import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('knygos.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table named 'knygos' with Lithuanian column names
cursor.execute('''
    CREATE TABLE IF NOT EXISTS knygos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Book ID (auto-incremented)
        pavadinimas TEXT NOT NULL,             -- Book title
        autorius TEXT NOT NULL                 -- Book author
    )
''')

# Commit the transaction to save changes
conn.commit()

# Close the connection to the database
conn.close()

print("Duomenų bazė ir lentelė sėkmingai sukurta.")  # Database and table created successfully
# This script initializes a SQLite database and creates a table for books with Lithuanian column names.