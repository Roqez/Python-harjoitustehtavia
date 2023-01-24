import random
tulos = 0
def silmaluku ():
    arvo = random.randint(1,6)
    return arvo


while tulos != 6:
    tulos = silmaluku()
    print("Heitit nopan luvun: "+str(tulos))

print("Jes! sait luvun: "+str(tulos))

