# logger.py

from datetime import datetime

def log_klaida(message):
    with open("errors.log", "a") as log_failas:
        log_failas.write(f"[{datetime.now()}] {message}\n")
