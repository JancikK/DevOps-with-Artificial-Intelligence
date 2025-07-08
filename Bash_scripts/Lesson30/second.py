# padalinti.py

def padalink_skaičius():
    try:
        # Ask user to input two numbers
        pirmas = float(input("Įveskite pirmą skaičių: "))
        antras = float(input("Įveskite antrą skaičių: "))

        # Perform division
        rezultatas = pirmas / antras
        print(f"{pirmas} padalintas iš {antras} yra {rezultatas}")

    except ZeroDivisionError:
        # Handle division by zero
        print("Klaida: dalyba iš nulio negalima.")

    except ValueError:
        # Handle invalid input (non-number)
        print("Klaida: įveskite tik skaičius.")

    except Exception as klaida:
        # Catch any unexpected errors
        print(f"Nenumatyta klaida: {klaida}")

# Run the function
if __name__ == "__main__":
    padalink_skaičius()
# This script defines a function to divide two numbers input by the user.
# It handles division by zero, invalid input, and other unexpected errors.