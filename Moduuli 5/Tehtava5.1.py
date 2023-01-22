import random
summa = 0
kerrat = int(input("Syötä noppien lukumäärä"))
heitot = []
for heitot in range(kerrat):
    heitto = random.randint(1, 6)
    summa = summa + heitto
print("Tämä on loppusumma "+str(summa))