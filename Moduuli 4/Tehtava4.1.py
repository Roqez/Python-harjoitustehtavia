luku = 0
toistot = 0
while toistot <1000:
    toistot = toistot + 1
    luku = luku +1
    while int(luku)%3 == 0:
        print("Luku "+str(luku)+" on kolmella jaollinen")
        luku = luku +1
        toistot = toistot + 1