# decorators.py

import time
from functools import wraps

# Decorator to measure execution time
def matuoti_laika(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        rezultatas = func(*args, **kwargs)
        end = time.time()
        print(f"Funkcija '{func.__name__}' įvykdyta per {end - start:.2f} sekundes.")
        return rezultatas
    return wrapper

# Decorator with a message argument
def su_žinute(žinutė):
    def dekoratorius(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{žinutė} (prieš vykdymą)")
            rezultatas = func(*args, **kwargs)
            print(f"{žinutė} (po vykdymo)")
            return rezultatas
        return wrapper
    return dekoratorius

# Class decorator to count method calls
def skaičiuoti_kvietimus(cls):
    class NaujaKlasė(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.kvietimai = {}

        def __getattribute__(self, name):
            attr = super().__getattribute__(name)
            if callable(attr) and not name.startswith("__"):
                self.kvietimai[name] = self.kvietimai.get(name, 0) + 1
            return attr
    return NaujaKlasė
