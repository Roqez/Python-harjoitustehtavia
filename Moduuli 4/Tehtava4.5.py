kayttaja = str("python")
salasana = str("rules")
yritykset = 0
kayttajansyote = None
salasanasyote = None

while yritykset < 5 :
    if kayttajansyote == kayttaja and salasanasyote == salasana:
        print("Tervetuloa!")
        break
    yritykset = yritykset + 1
    kayttajansyote = input("Syötä käyttäjätunnus")
    salasanasyote = input("Syötä salasana")

else:
    print("Pääsy evätty!")
