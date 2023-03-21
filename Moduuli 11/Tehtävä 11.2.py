import random
class auto:
    def __init__(self, rekisteritunnus,huippunopeus,nopeus,kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

    def kiihdytä(self):
        nopeus = random.randint(-10, 15)
        if nopeus <= self.huippunopeus and nopeus < self.huippunopeus:
            self.nopeus = self.nopeus + nopeus
            if self.nopeus >= self.huippunopeus:
                self.nopeus = self.huippunopeus
            elif self.nopeus < 0:
                self.nopeus = 0
        else:
            print(
                f"Virheellinen kiihdytyksen arvo, arvosi oli {nopeus} sen pitää olla alle {self.huippunopeus}")
        print("Nopeus: " + str(self.nopeus) + " km/h")

    def kulje(self):
        self.kuljettumatka = self.kuljettumatka + self.nopeus * 1


class Sähköauto(auto):
    def __init__(self,rekisteritunnus,huippunopeus,nopeus,akkukapasiteetti,kuljettumatka):
        super().__init__(rekisteritunnus,huippunopeus,nopeus,kuljettumatka)
        self.akkukapasiteetti = akkukapasiteetti
class Polttomoottoriauto(auto):
    def __init__(self,rekisteritunnus,huippunopeus,nopeus,bensatankki,kuljettumatka):
        super().__init__(rekisteritunnus,huippunopeus,nopeus,kuljettumatka)
        self.bensatankki = bensatankki

sähköautot = []
bensiiniautot = []
sähköauto1 = Sähköauto("ABC-15",180,100,52.5,0)
bensiiniauto1 = Polttomoottoriauto("ACD-123",165,100,32.3,0)
sähköautot.append(sähköauto1)
bensiiniautot.append(bensiiniauto1)
for i in range(3):
    bensiiniauto1.kulje()
    sähköauto1.kulje()
print(f"Rekisterinumerolla {sähköauto1.rekisteritunnus} varustettu sähköauton mittarilukema on: {sähköauto1.kuljettumatka} km")
print(f"Rekisterinumerolla {bensiiniauto1.rekisteritunnus} varustettu bensiiniauton mittarilukema on: {bensiiniauto1.kuljettumatka} km")


