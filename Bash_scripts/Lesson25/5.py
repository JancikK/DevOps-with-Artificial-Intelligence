studentas = {
    "vardas": "Tomas",           # Student's name
    "amžius": 17,                # Student's age
    "klasė": "11B",              # Student's class
    "dalykai": {                 # Dictionary of subjects and grades
        "Matematika": "9",
        "Anglų": "8"
    }
}

studentas["dalykai"]["Biologija"] = "10"  # Add a new subject and grade

print("Studento informacija:")     # Print student info
print(studentas)
