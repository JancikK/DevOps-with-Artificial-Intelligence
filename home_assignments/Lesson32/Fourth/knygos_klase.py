# Sukuriame bazinę klasę Knyga (Book)
class Knyga:
    def __init__(self, pavadinimas, autorius):
        self.pavadinimas = pavadinimas
        self.autorius = autorius

    def __str__(self):
        return f"Knyga: '{self.pavadinimas}', autorius: {self.autorius}"


# Sukuriame paveldėtą klasę ElektronineKnyga (ElectronicBook)
class ElektronineKnyga(Knyga):
    def __init__(self, pavadinimas, autorius, failo_formatas):
        super().__init__(pavadinimas, autorius)
        self.failo_formatas = failo_formatas

    def __str__(self):
        return f"E-Knyga: '{self.pavadinimas}', autorius: {self.autorius}, formatas: {self.failo_formatas}"


# Sukuriame objektus ir atspausdiname jų informaciją
k1 = Knyga("Altorių šešėly", "Vincas Mykolaitis")
k2 = ElektronineKnyga("Mažasis princas", "Antoine de Saint-Exupéry", "pdf")

print(k1)
print(k2)
# Išvedimas:
# Knyga: 'Altorių šešėly', autorius: Vincas
