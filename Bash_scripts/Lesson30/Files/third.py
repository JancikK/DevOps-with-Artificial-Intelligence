# third.py


import os
import argparse

def pervadinti_txt_failus(katalogas, priesaga):
    try:
        # Get all files in the specified directory
        visi_failai = os.listdir(katalogas)
        print(f"Failai kataloge: {visi_failai}")

        # Filter only .txt files
        txt_failai = [failas for failas in visi_failai if failas.endswith(".txt")]
        print(f"Rasti .txt failai: {txt_failai}")

        for indeksas, failas in enumerate(txt_failai):
            senas_kelias = os.path.join(katalogas, failas)
            naujas_vardas = f"{priesaga}_{indeksas + 1}.txt"
            naujas_kelias = os.path.join(katalogas, naujas_vardas)

            # Rename the file
            os.rename(senas_kelias, naujas_kelias)
            print(f"Pervadintas: {failas} → {naujas_vardas}")

    except FileNotFoundError:
        print("Klaida: katalogas nerastas.")
    except Exception as klaida:
        print(f"Nenumatyta klaida: {klaida}")

if __name__ == "__main__":
    # Set up command-line arguments
    parseris = argparse.ArgumentParser(description="Pervadinti visus .txt failus kataloge.")
    parseris.add_argument("katalogas", help="Kelias iki katalogo su .txt failais")
    parseris.add_argument("priesaga", help="Naujas vardas prieš failo numerį")

    # Parse arguments and run the function
    argumentai = parseris.parse_args()
    pervadinti_txt_failus(argumentai.katalogas, argumentai.priesaga)
