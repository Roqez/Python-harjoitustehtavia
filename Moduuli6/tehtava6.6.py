import math
def pizza(halkaisija,hinta):
    sade = halkaisija/2
    pizzanAla = math.pi*sade**2
    yksikkohinta = pizzanAla/hinta#Kertoo pizzan hinnan per neliömetri
    return yksikkohinta


def main():
    halkaisija = int(input("Syötä ensimmäisen pizzan halkaisija senttimetreinä "))
    hinta = int(input("Syötä ensimmäisen pizzan hinta euroina "))
    ensimmainen_pizza = pizza(halkaisija,hinta)
    print (ensimmainen_pizza)
    halkaisija = int(input("Syötä toisen pizzan halkaisija senttimetreinä "))
    hinta = int(input("Syötä toisen pizzan hinta euroina "))
    toinen_pizza = int(pizza(halkaisija,hinta))
    print(toinen_pizza)
    if ensimmainen_pizza > toinen_pizza:
        print(ensimmainen_pizza)
        print(toinen_pizza)
        print("Toinen pizza antaa paremman vastineen rahalle")
    else:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle")



main()
