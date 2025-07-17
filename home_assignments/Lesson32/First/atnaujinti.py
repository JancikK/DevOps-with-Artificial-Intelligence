import sqlite3

# Connect to the existing database
conn = sqlite3.connect('knygos.db')
cursor = conn.cursor()

# Update the author of a specific book
cursor.execute("""
    UPDATE knygos
    SET autorius = ?
    WHERE pavadinimas = ?
""", ("Antuanas de Sent-Egziuperi", "Mažasis princas"))

# Save changes
conn.commit()
conn.close()

print("Autorius sėkmingai atnaujintas.")  # Author successfully updated
