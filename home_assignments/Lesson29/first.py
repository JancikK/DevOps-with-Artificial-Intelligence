# Define a class called Persona
class Persona:
    # Constructor method to initialize the object
    def __init__(self, vardas, amzius):
        # Private attributes (cannot be accessed directly from outside the class)
        self.__vardas = vardas
        self.__amzius = amzius

    # Getter method for the 'vardas' attribute
    def gauti_varda(self):
        # Return the private attribute vardas
        # This method allows controlled access to the private attribute
        return self.__vardas

    # Setter method for the 'vardas' attribute
    def irasyti_varda(self, naujas_vardas):
        # Update the private attribute __vardas with the new value
        self.__vardas = naujas_vardas

    # Getter method for the 'amzius' attribute
    def gauti_amziu(self):
        # Return the private attribute __amzius
        # This method allows controlled access to the private attribute
        return self.__amzius

    # Setter method for the 'amzius' attribute
    def irasyti_amziu(self, naujas_amzius):
        # Validate that the age is not negative
        if naujas_amzius >= 0:
            # If valid, update the private attribute __amzius
            self.__amzius = naujas_amzius
        else:
            # If not valid, print an error message
            print("Amžius negali būti neigiamas!")

# ----------------------
# Example usage of the Persona class

# Create an instance of Persona with initial values
p = Persona("Sandra", 23)

# Print the name and age using the getter methods
print("Vardas:", p.gauti_varda())   # Output: Sandra
print("Amžius:", p.gauti_amziu())     # Output: 23

# Use setter methods to change the name and age
p.irasyti_varda("Janas")              # Change name to Janas
p.irasyti_amziu(24)                  # Change age to 24

# Print the updated name and age
print("Naujas vardas:", p.gauti_varda())  # Output: Janas
print("UNaujas Amžius:", p.gauti_amziu())    # Output: 24

# Optional test: Try setting a negative age
p.irasyti_amziu(-10)  # This will trigger the validation message