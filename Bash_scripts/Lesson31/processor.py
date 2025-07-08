import os
import csv
import requests
import numpy as np
from datetime import datetime
from decorators import su_žinute, matuoti_laika, skaičiuoti_kvietimus
from logger import log_klaida

@skaičiuoti_kvietimus
class WebDataProcessor:

    def __init__(self, folder_path=".", log_failas_vardas="default"):
        self.katalogas = folder_path
        self.csv_failas = os.path.join(self.katalogas, "output.csv")

        # Create log folder and prepare log path
        log_folderis = os.path.join(self.katalogas, "log")
        os.makedirs(log_folderis, exist_ok=True)
        self.log_failas = os.path.join(log_folderis, f"{log_failas_vardas}_output.log")

    @su_žinute("Atliekamas svetainės užklausa")
    @matuoti_laika
    def gauti_duomenis(self, url):
        try:
            atsakas = requests.get(url)
            atsakas.raise_for_status()

            with open(self.csv_failas, "w", newline="", encoding="utf-8") as csv_failas:
                writer = csv.writer(csv_failas)
                for eilute in atsakas.text.splitlines():
                    writer.writerow([eilute])
            print(f"Duomenys įrašyti į: {self.csv_failas}")

            # Log success
            with open(self.log_failas, "a", encoding="utf-8") as logas:
                logas.write(f"[{datetime.now()}] Sėkminga užklausa: {url}\n")

        except Exception as klaida:
            print("Klaida užklausiant svetainės.")
            log_klaida(str(klaida))
            with open(self.log_failas, "a", encoding="utf-8") as logas:
                logas.write(f"[{datetime.now()}] Klaida: {klaida}\n")

    @su_žinute("Analizuojamas CSV failas")
    def analizuoti_csv(self):
        try:
            suvestine = np.genfromtxt(self.csv_failas, delimiter="\n", dtype=str, encoding="utf-8")
            eiluciu_sk = len(suvestine)
            print(f"Failas turi {eiluciu_sk} eilutes.")

            # Log row count
            with open(self.log_failas, "a", encoding="utf-8") as logas:
                logas.write(f"[{datetime.now()}] CSV eilučių skaičius: {eiluciu_sk}\n")

        except Exception as klaida:
            print("Klaida skaitant CSV failą.")
            log_klaida(str(klaida))
            with open(self.log_failas, "a", encoding="utf-8") as logas:
                logas.write(f"[{datetime.now()}] Klaida skaitant CSV: {klaida}\n")
