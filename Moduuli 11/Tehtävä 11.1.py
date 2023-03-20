class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"Teoksen nimi on {self.nimi}")

class Kirja (Julkaisu):
    def __init__(self,nimi,kirjoittaja,sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjan kirjoittaja on {self.kirjoittaja} ja sivumäärä on {self.sivumäärä}")
class Lehti (Julkaisu):
    def __init__(self,nimi,päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Lehden päätoimittaja on {self.päätoimittaja}")

Julkaisut = []
Julkaisut.append(Lehti("Aku Ankka","Aki Hyyppä"))
Julkaisut.append(Kirja("Hytti n:o 6","Rosa Liksom","200 sivua"))
for i in Julkaisut:
    i.tulosta_tiedot()
