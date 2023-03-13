import random
class auto:
    def __init__(self, rekisteritunnus,huippunopeus,nopeus,kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka
    def kiihdytä(self,nopeudenmuutos):
        if nopeudenmuutos <= self.huippunopeus and nopeudenmuutos < self.huippunopeus:
            self.nopeus = self.nopeus + nopeudenmuutos
            if self.nopeus >= self.huippunopeus:
                self.nopeus = self.huippunopeus
            elif self.nopeus < 0:
                self.nopeus = 0
        else:
            print(f"Virheellinen kiihdytyksen arvo, arvosi oli {nopeudenmuutos} sen pitää olla alle {self.huippunopeus}")
        print("Nopeus: "+str(self.nopeus)+" km/h")
    def kulje(self,aika):
        self.kuljettumatka = self.kuljettumatka + self.nopeus * aika
        print("Kuljettumatka: "+str(self.kuljettumatka)+" km")

autot = []
kuljettumatka = 0
for i in range (1,11):
    rekisteritunnus = "ABC-"+str(i)
    huippunopeus = random.randint(100,200)
    kaara = auto(rekisteritunnus,huippunopeus,0,0)
    autot.append(kaara)

while kuljettumatka < 10000:
    for i in autot:
        nopeus = random.randint(-10,15)
        i.kiihdytä(nopeus)
        i.kulje(1)
        print(i.rekisteritunnus)
        if i.kuljettumatka >= 10000:
            kuljettumatka = i.kuljettumatka
            print("Kilpailun voittaja on kisaaja rekisterinumerolla: "+str(i.rekisteritunnus))
            break

