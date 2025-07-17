import math  # Used for math.pi in circle area calculation

# Base class: general shape
class Figura:
    def plotas(self):
        # Default area if not overridden
        return 0

# Subclass: Rectangle
class Staciakampis(Figura):
    def __init__(self, plotis, aukstis):
        # Store width and height
        self.plotis = plotis
        self.aukstis = aukstis

    def plotas(self):
        # Area of rectangle = width * height
        return self.plotis * self.aukstis

# Subclass: Circle
class Apskritimas(Figura):
    def __init__(self, spindulys):
        # Store radius
        self.spindulys = spindulys

    def plotas(self):
        # Area of circle = π * radius^2
        return math.pi * self.spindulys ** 2

# ----------------------
# User input section

# Ask user to input dimensions for rectangle
plotis = float(input("Įveskite stačiakampio plotį: "))   # "Enter rectangle width"
aukstis = float(input("Įveskite stačiakampio aukštį: ")) # "Enter rectangle height"

# Ask user to input radius for circle
spindulys = float(input("Įveskite apskritimo spindulį: "))  # "Enter circle radius"

# Create rectangle and circle objects with user input
staciakampis = Staciakampis(plotis, aukstis)
apskritimas = Apskritimas(spindulys)

# Print calculated area for both shapes
print("Stačiakampio plotas:", staciakampis.plotas())  # Rectangle area
print("Apskritimo plotas:", round(apskritimas.plotas(), 2))  # Circle area (rounded to 2 decimal places)
