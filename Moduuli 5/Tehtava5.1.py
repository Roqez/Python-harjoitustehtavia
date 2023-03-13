import random
summa = 0
kerrat = int(input("Syötä noppien lukumäärä"))
for i in range(kerrat):
    heitto = random.randint(1, 6)
    print(heitto)
    summa = heitto + summa
print("Tämä on loppusumma "+str(summa))