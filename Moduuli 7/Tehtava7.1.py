def tell_season(jarjestysnumero):
    vuodenajat = ("Talvi","Kevät","Kesä","Syksy")
    if jarjestysnumero == "12" or jarjestysnumero == "1" or jarjestysnumero == "2":
        vuodenaika = vuodenajat[0]
    elif jarjestysnumero == "3" or jarjestysnumero == "4" or jarjestysnumero == "5":
        vuodenaika = vuodenajat[1]
    elif jarjestysnumero == "6" or jarjestysnumero == "7" or jarjestysnumero == "8":
        vuodenaika = vuodenajat[2]
    elif jarjestysnumero == "9" or jarjestysnumero == "10" or jarjestysnumero == "11":
        vuodenaika = vuodenajat[3]
    return vuodenaika
def main():
    syotettynumero = input("Syötä kuukauden järjestysnumero")
    print (tell_season(syotettynumero))


main()