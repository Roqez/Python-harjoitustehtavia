import random
luku = random.randint(1,10)
arvaus = None
while arvaus != luku:
    arvaus = int(input("Arvaa numero"))
    if arvaus > luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
else:
    print("Oikein arvattu!")
