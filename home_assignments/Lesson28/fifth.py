# Task 5: Bank account class with deposit, withdraw, and balance checking

class BankoSaskaita:
    def __init__(self, savininkas, balansas=0):
    
        self.savininkas = savininkas
        self.balansas = balansas

    def inesti(self, suma):
        
        self.balansas += suma

    def isimti(self, suma):
        if suma > self.balansas:
            print("Nepakanka lesu.")
        else:
            self.balansas -= suma

    def parodyti_balansa(self):
        print(f"Balansas: {self.balansas} €")
