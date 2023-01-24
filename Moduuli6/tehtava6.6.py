import math
def pizza(halkaisija,hinta):
    sade = halkaisija/50 #Laskee halkaisijasta säteen ja muuttaa myös tuloksen metreiksi
    pizzanAla = math.pi*sade**2
    yksikkohinta = hinta/pizzanAla
    return yksikkohinta

def main():
    halkaisija = int(input("Syötä pizzan halkaisija senttimetreinä "))
    hinta = int(input("Syötä pizzan hinta euroina "))
    print(f"Pizzan hinta on {pizza(halkaisija,hinta):5.2f} euroa")


main()
