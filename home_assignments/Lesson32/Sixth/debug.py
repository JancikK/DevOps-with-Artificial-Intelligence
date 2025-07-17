import requests
from bs4 import BeautifulSoup

# Naudojame fiksuotą miestą su žinomu ID
miestas = "vilnius"
url = f'https://www.timeanddate.com/weather/lithuania/vilnius'

# Gauname HTML atsakymą
atsakymas = requests.get(url)
soup = BeautifulSoup(atsakymas.text, 'html.parser')

# Išsaugome visą HTML į failą debug purposes
with open("debug.html", "w", encoding="utf-8") as failas:
    failas.write(soup.prettify())
    print("HTML išsaugotas kaip debug.html")
