# Task 3: Rectangle class with length and width, with methods for area and perimeter

class Staciakampis:
    def __init__(self, ilgis, plotis):
        # Initialize the rectangle with length and width
        self.ilgis = ilgis
        self.plotis = plotis

    def plotas(self):
        return self.ilgis * self.plotis
        # Area calculation: length * width
    def perimetras(self):
        return 2 * (self.ilgis + self.plotis)
        # Perimeter calculation: 2 * (length + width)