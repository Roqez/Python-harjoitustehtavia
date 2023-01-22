luku = int(input("Syötä lukuja, kun olet valmis paina Enter"))
luvut = [luku]
while True:
    luku = input("Syötä lukuja, kun olet valmis paina Enter")
    if luku == '':
        break
    if int(luku) != '':
        luku = int(luku)
        luvut.append(luku)
luvut.sort(reverse=True)
print(luvut)