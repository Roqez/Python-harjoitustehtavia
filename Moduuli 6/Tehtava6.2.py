import random
def silmaluku (tahkot):
    arvo = random.randint(1,tahkot)
    return arvo


tulos = 0
tahkot = int(input("Syötä nopan tahkojen määrä"))
while tulos != tahkot:
    silmaluku(tahkot)
    tulos = silmaluku(tahkot)
    print("Heitit nopan luvun: "+str(tulos))

print("Jes! sait luvun: "+str(tulos))

