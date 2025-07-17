# SQLAlchemy užduotis — mokomasis failas


Šiame faile bus atliekami pagrindiniai SQLAlchemy veiksmai:
1. Sukuriama SQLite duomenų bazė ir lentelė "knygos.db"
2. Įrašomos kelios knygos
3. Parodomi visi įrašai
4. Atnaujinamas vienas įrašas
5. Ištrinamas vienas įrašas


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Sukuriame bazinę ORM klasę
Bazinis = declarative_base()

# 2. Apibrėžiame lentelės modelį
class Knyga(Bazinis):
    __tablename__ = 'knygos'
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String, nullable=False)
    autorius = Column(String, nullable=False)

    def __repr__(self):
        return f"<Knyga(id={self.id}, pavadinimas='{self.pavadinimas}', autorius='{self.autorius}')>"

# 3. Sukuriame duomenų bazės variklį ir sesiją
variklis = create_engine('sqlite:///knygos.db')
Bazinis.metadata.create_all(variklis)
Sesija = sessionmaker(bind=variklis)
sesija = Sesija()

# 4. Įrašome keletą knygų
knyga1 = Knyga(pavadinimas="Balta drobulė", autorius="Antanas Škėma")
knyga2 = Knyga(pavadinimas="Tūla", autorius="Jurgis Kunčinas")
sesija.add_all([knyga1, knyga2])
sesija.commit()

# 5. Parodome visus įrašus
print("\nVISOS KNYGOS:")
for knyga in sesija.query(Knyga).all():
    print(knyga)

# 6. Atnaujiname įrašą
knyga_atnaujinti = sesija.query(Knyga).filter_by(pavadinimas="Tūla").first()
if knyga_atnaujinti:
    knyga_atnaujinti.autorius = "J. Kunčinas (atnaujinta)"
    sesija.commit()
    print("\nKnyga atnaujinta:", knyga_atnaujinti)

# 7. Ištriname įrašą
knyga_trinti = sesija.query(Knyga).filter_by(pavadinimas="Balta drobulė").first()
if knyga_tr