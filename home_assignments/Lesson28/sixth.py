# Task 6: Car class with __str__ and __repr__

class Automobilis:
    def __init__(self, marke, modelis, metai):
        #___init___ initializes the car with its brand, model, and year
        self.marke = marke
        self.modelis = modelis
        self.metai = metai

    def __str__(self):
        # Human-readable format
        return f"{self.metai} {self.marke} {self.modelis}"

    def __repr__(self):
        # Developer-friendly format
        return f"Automobilis(marke='{self.marke}', modelis='{self.modelis}', metai={self.metai})"
