import random
def silmaluku ():
    arvo = random.randint(1,6)
    return arvo


tulos = 0
while tulos != 6:
    silmaluku()
    tulos = silmaluku()
    print("Heitit nopan luvun: "+str(tulos))

print("Jes! sait luvun: "+str(tulos))

