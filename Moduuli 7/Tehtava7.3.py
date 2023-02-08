lentoasemat = {}
syote = None
def syotto():
    ICAO = input("Syötä ICAO koodi")
    nimi = input ("Syötä lentoaseman nimi")
    lentoasemat [ICAO] = nimi
    return lentoasemat

def haku():
    hakukysymys = input("Syötä ICAO koodi niin haen sitä vastaavan lentokentän")
    if hakukysymys in lentoasemat:
        print(f"Koodia {hakukysymys} vastaa lentoasema {lentoasemat[hakukysymys]}")



while syote != "lopeta":
    syote = input("Mitä haluat tehdä?: syötä/hae/lopeta")
    if syote == "syötä":
        syotto()
        lentoasemat = lentoasemat
    elif syote == "hae":
        haku()
    elif syote == "lopeta":
        print("Kiitos käytöstä")


