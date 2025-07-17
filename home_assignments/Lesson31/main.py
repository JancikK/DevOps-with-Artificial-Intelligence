from processor import WebDataProcessor

if __name__ == "__main__":
    svetaine = input("Įveskite svetainės URL (pvz. https://example.com): ").strip()
    failo_vardas = input("Įveskite log failo vardą (be .log): ").strip()

    apdorotuvas = WebDataProcessor(log_failas_vardas=failo_vardas)
    apdorotuvas.gauti_duomenis(svetaine)
    apdorotuvas.analizuoti_csv()

    print(f"Klasės metodų kvietimų statistika: {apdorotuvas.kvietimai}")
