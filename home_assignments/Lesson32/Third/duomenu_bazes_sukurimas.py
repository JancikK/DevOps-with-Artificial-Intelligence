from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the base class for ORM
Bazinis = declarative_base()

# Define the table model
class Knyga(Bazinis):
    __tablename__ = 'knygos'  # Table name in the database

    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String, nullable=False)
    autorius = Column(String, nullable=False)

    def __repr__(self):
        return f"<Knyga(id={self.id}, pavadinimas='{self.pavadinimas}', autorius='{self.autorius}')>"

# Create the SQLite database engine
variklis = create_engine('sqlite:///knygos.db')

# Create the table(s) based on the model
Bazinis.metadata.create_all(variklis)

# Create a session factory and session object
Sesija = sessionmaker(bind=variklis)
sesija = Sesija()

# Add sample book records
knyga1 = Knyga(pavadinimas="Altorių šešėly", autorius="Vincas Mykolaitis-Putinas")
knyga2 = Knyga(pavadinimas="Mažasis princas", autorius="Antoine de Saint-Exupéry")

# Add and commit to the database
sesija.add_all([knyga1, knyga2])
sesija.commit()

print("Knygos sėkmingai įrašytos į duomenų bazę.")

# Query and print all books
knygos = sesija.query(Knyga).all()
print("Visos knygos duomenų bazėje:")
for knyga in knygos:
    print(knyga)
