# Base class: Person
class Zmogus:
    def __init__(self, vardas, amzius):
        # Store name and age
        self.vardas = vardas
        self.amzius = amzius

    def info(self):
        # Return person info
        return f"Vardas: {self.vardas}, Amžius: {self.amzius}"

# Subclass: Student
class Studentas(Zmogus):
    def __init__(self, vardas, amzius, matematika, informatika, fizika):
        # Initialize parent class
        super().__init__(vardas, amzius)
        # Store grades for 3 disciplines
        self.matematika = matematika
        self.informatika = informatika
        self.fizika = fizika

    def vidurkis(self):
        # Calculate average of 3 grades
        return round((self.matematika + self.informatika + self.fizika) / 3, 2)

    def info(self):
        # Return detailed student info
        return (
            f"Vardas: {self.vardas}, Amžius: {self.amzius}, "
            f"Matematika: {self.matematika}, Informatika: {self.informatika}, Fizika: {self.fizika}, "
            f"Vidurkis: {self.vidurkis()}"
        )

# ----------------------
# User input section

vardas = input("Įveskite studento vardą: ")
amzius = int(input("Įveskite studento amžių: "))

# Input 3 subject grades
matematika = float(input("Įveskite pažymį iš matematikos: "))
informatika = float(input("Įveskite pažymį iš informatikos: "))
fizika = float(input("Įveskite pažymį iš fizikos: "))

# Create student object
studentas = Studentas(vardas, amzius, matematika, informatika, fizika)

# Output full student info
print(studentas.info())
