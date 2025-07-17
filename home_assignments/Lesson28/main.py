# Main test script that brings everything together

from first import pasisveikinimas
from second import Gyvunas
from third import Staciakampis
from utils.fourth import faktorialas
from fifth import BankoSaskaita
from sixth import Automobilis
#dont use numbers to name files, its harder to use it code XD) 

# Task 1: Hello World
pasisveikinimas()

# Task 2: Create an animal and make it speak
kate = Gyvunas("Miau")
kate.skleisti_garsa()

# Task 3: Create a rectangle and calculate area and perimeter
didele_deze = Staciakampis(10, 5)
print("Plotas:", didele_deze.plotas())
print("Perimetras:", didele_deze.perimetras())

# Task 4: Use factorial function
print("Faktorialas 5:", faktorialas(5))

# Task 5: Use Bank account
saskaita = BankoSaskaita("Jonas", 100)
saskaita.inesti(50)
saskaita.isimti(30)
saskaita.parodyti_balansa()

# Task 6: Car object with __str__ and __repr__
masina = Automobilis("Toyota", "Corolla", 2025)
print(masina)
print(repr(masina))
