nimet = set()
nimi = None

while nimi != "":
    nimi = input("Syötä nimi")
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
        nimet.add(nimi)
    else:
        print("Uusi nimi")
        nimet.add(nimi)

for n in nimet:
    print(n)
