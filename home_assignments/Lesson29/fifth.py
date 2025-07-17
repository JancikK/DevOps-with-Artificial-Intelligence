import math  # for math.pi

# Base class: generic shape
class Figura:
    def plotas(self):
        # Default area if not overridden
        return 0

    def perimetras(self):
        # Default perimeter if not overridden
        return 0

# Subclass: Rectangle (Stačiakampis)
class Staciakampis(Figura):
    def __init__(self, plotis, aukstis):
        self.plotis = plotis
        self.aukstis = aukstis

    def plotas(self):
        # Area = width * height
        return self.plotis * self.aukstis

    def perimetras(self):
        # Perimeter = 2 * (width + height)
        return 2 * (self.plotis + self.aukstis)

# Subclass: Circle (Apskritimas)
class Apskritimas(Figura):
    def __init__(self, spindulys):
        self.spindulys = spindulys

    def plotas(self):
        # Area = π * radius^2
        return math.pi * self.spindulys ** 2

    def perimetras(self):
        # Perimeter = 2 * π * radius
        return 2 * math.pi * self.spindulys

# ----------------------
# Example usage

# Rectangle with user input
plotis = float(input("Įveskite stačiakampio plotį: "))
aukstis = float(input("Įveskite stačiakampio aukštį: "))
staciakampis = Staciakampis(plotis, aukstis)

# Circle with user input
spindulys = float(input("Įveskite apskritimo spindulį: "))
apskritimas = Apskritimas(spindulys)

# Print results
print("\n--- Stačiakampis ---")
print("Plotas:", staciakampis.plotas())
print("Perimetras:", staciakampis.perimetras())

print("\n--- Apskritimas ---")
print("Plotas:", round(apskritimas.plotas(), 2))
print("Perimetras:", round(apskritimas.perimetras(), 2))
