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


auto1 = auto("ABC-123",142,0,0)
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
auto1.kiihdytä(-50)
auto1.kiihdytä(150)
auto1.kiihdytä(-200)