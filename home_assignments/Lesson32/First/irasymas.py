import sqlite3

# Connect to the existing database
conn = sqlite3.connect('knygos.db')
cursor = conn.cursor()

# Insert Lithuanian books
knygos = [
    ("Altorių šešėly", "Vincas Mykolaitis-Putinas"),
    ("Mažasis princas", "Antoine de Saint-Exupéry"),
    ("Dievų miškas", "Balys Sruoga")
]

cursor.executemany("INSERT INTO knygos (pavadinimas, autorius) VALUES (?, ?)", knygos)

conn.commit()
conn.close()

print("Knygos sėkmingai įrašytos į duomenų bazę.")
# This script inserts a list of Lithuanian books into the existing SQLite database 'knygos.db'.