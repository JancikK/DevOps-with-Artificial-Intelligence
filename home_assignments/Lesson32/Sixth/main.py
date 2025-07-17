import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Vartotojo įvestis
salis = input("Įveskite šalį (pvz., lithuania): ").strip().lower()
miestas = input("Įveskite miestą (pvz., vilnius): ").strip().lower()

# Sukuriame URL
url = f"https://www.timeanddate.com/weather/{salis}/{miestas}"

# HTTP užklausa
atsakymas = requests.get(url)
soup = BeautifulSoup(atsakymas.text, 'html.parser')

# Ieškome temperatūros ir aprašymo
temp_elem = soup.find('div', id='qlook')

# Data ir laikas dabar
now = datetime.now()
data_str = now.strftime("%Y-%m-%d")
laikas_str = now.strftime("%H:%M:%S")

if temp_elem:
    temperatura = temp_elem.find('div', class_='h2').text.strip()
    aprasymas = temp_elem.find('p').text.strip()
    orai_str = f"{miestas.title()}, {salis.title()} — {temperatura}, {aprasymas}"
else:
    orai_str = f"Nepavyko rasti orų duomenų miestui: {miestas.title()}, šaliai: {salis.title()}"

# Failo pavadinimas su data
failo_pavadinimas = f"{salis}_{miestas}_{data_str}.txt"

# Išsaugome rezultatą į failą su data ir laiku
with open(failo_pavadinimas, "w", encoding="utf-8") as failas:
    failas.write(f"{data_str} - {laikas_str} - {orai_str}\n")
    print(f"Rezultatas išsaugotas faile: {failo_pavadinimas}")