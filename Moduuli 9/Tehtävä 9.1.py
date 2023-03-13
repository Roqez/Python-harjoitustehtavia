class auto:
    def __init__(self, rekisteritunnus,huippunopeus,nopeus,kuljettumatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

auto1 = auto("ABC-123",142,0,0)
print(f"Auton rekisteritunnus on {auto1.rekisteritunnus}, huippunopeus: {auto1.huippunopeus} km/h, nopeus: {auto1.nopeus}, kuljettumatka: {auto1.kuljettumatka}")
