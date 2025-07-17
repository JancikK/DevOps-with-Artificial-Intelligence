# How to use
# 1
    >Python3 duomenu_bazes_sukurimas
# Sukure duomenu baze
# 2
    >python3 irasymas.py
# Iraso informacija
# 3
# Perziureti
    >python3
>
Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import sqlite3
... conn = sqlite3.connect('knygos.db')
... cursor = conn.cursor()
... cursor.execute("SELECT * FROM knygos")
... print(cursor.fetchall())
... 
[(1, 'Altorių šešėly', 'Vincas Mykolaitis-Putinas'), (2, 'Mažasis princas', 'Antoine de Saint-Exupéry'), (3, 'Dievų miškas', 'Balys Sruoga')]
>>> 
# Arba paleisti
    > python3 gauti_informacija.py


