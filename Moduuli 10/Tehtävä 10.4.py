import random
class kilpailu:
    def __init__(self,nimi,pituus,autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for i in self.autot:
            i.kiihdytä()
            i.kulje()
    def tulosta_tilanne(self):
        for i in self.autot:
            print("Rekisterinumero " + i.rekisteritunnus + " Huippunopeus " + str(
                i.huippunopeus) + "km/h" + " Nopeus " + str(i.nopeus) + "km/h" + " Kuljettumatka " + str(
                i.kuljettumatka) + "km")
    def kilpailu_ohi(self):
        for i in autot:
            if i.kuljettumatka >= self.pituus:
                print("Kilpailun voittaja on kisaaja rekisterinumerolla: " + str(i.rekisteritunnus))
                return True

class auto:
    def __init__(self, rekisteritunnus,huippunopeus,nopeus,kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka
    def __repr__(self):
        return "Rekisterinumero "+self.rekisteritunnus+" Huippunopeus "+str(self.huippunopeus)+"km/h"+" Nopeus "+str(self.nopeus)+"km/h"+" Kuljettumatka "+str(self.kuljettumatka)+"km"
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
        print("Kuljettumatka: "+str(self.kuljettumatka)+" km")

autot = []
for i in range (1,11):
    rekisteritunnus = "ABC-"+str(i)
    huippunopeus = random.randint(100,200)
    kaara = auto(rekisteritunnus,huippunopeus,0,0)
    autot.append(kaara)

suuri_romuralli = kilpailu("Suuri Romuralli",8000,autot)

while True:
    for i in range(9):
        suuri_romuralli.tunti_kuluu()
        if suuri_romuralli.kilpailu_ohi():
            break
        suuri_romuralli.tulosta_tilanne()
    suuri_romuralli.tulosta_tilanne()
    if suuri_romuralli.kilpailu_ohi():
        break





