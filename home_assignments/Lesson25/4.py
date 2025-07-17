vaisiai = ["obuolys", "bananas", "kriaušė", "vyšnia", "apelsinas"]  # Create a list

vaisiai.append("arbūzas")      # Add new item to the list
vaisiai.remove("kriaušė")      # Remove an item by value
vaisius = vaisiai[2]           # Access element at index (couniting from 0 (so always -1))

print("Atnaujintas vaisių sąrašas:", vaisiai)  # Print updated list
print("Elementas su indeksu 2:", vaisius)      # Print accessed element
