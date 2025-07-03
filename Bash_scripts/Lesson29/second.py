# Parent class (base class)
class Gyvunas:  # "Animal"
    def sako(self):  # "speak"
        # Default behavior if not overridden
        return "Nežinomas gyvūno garsas"  # "Unknown animal sound"

# Subclass: Suo inherits from Gyvunas
class Suo(Gyvunas):  # "Dog"
    def sako(self):  # override method
        return "Au au!"  # Dog sound

# Subclass: Katinas inherits from Gyvunas
class Katinas(Gyvunas):  # "Cat"
    def sako(self):  # override method
        return "Miau!"  # Cat sound

# ----------------------
# Example usage of Gyvunas class

# Create instances of each class
gyvunas = Gyvunas()
suo = Suo()
katinas = Katinas()

# Call the speak method
print("Gyvūnas:", gyvunas.sako())   # Output: Unknown animal sound
print("Šuo:", suo.sako())           # Output: Au au!
print("Katinas:", katinas.sako())   # Output: Miau!
