vuodenajat = ("Talvi","Kevät","Kesä","Syksy")
numero = int(input("Syötä kuukauden järjestysnumero niin kerron sitä vastaavan vuoden ajan"))

if numero == 1 or numero == 2 or numero == 12:
    print(vuodenajat[0])
if numero == 3 or numero == 4 or numero == 5:
    print(vuodenajat[1])
if numero == 6 or numero == 7 or numero == 8:
    print(vuodenajat[2])
if numero == 9 or numero == 10 or numero == 11:
    print (vuodenajat[3])