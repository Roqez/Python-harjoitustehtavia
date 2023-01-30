import math
def pizza(halkaisija,hinta):
    sade = halkaisija/2
    sade_metreina = sade*0.01
    pizzanAla = math.pi*sade_metreina**2
    yksikkohinta = pizzanAla/hinta#Kertoo pizzan hinnan per neliömetri
    return yksikkohinta


def main():
    halkaisija = float(input("Syötä ensimmäisen pizzan halkaisija senttimetreinä "))
    hinta = float(input("Syötä ensimmäisen pizzan hinta euroina "))
    ensimmainen_pizza = pizza(halkaisija,hinta)
    halkaisija = float(input("Syötä toisen pizzan halkaisija senttimetreinä "))
    hinta = float(input("Syötä toisen pizzan hinta euroina "))
    toinen_pizza = pizza(halkaisija,hinta)
    if ensimmainen_pizza < toinen_pizza:
        print("Toinen pizza antaa paremman vastineen rahalle")
    else:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle")


main()
