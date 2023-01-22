luku = int(input("Syötä kokonaisluku"))

if luku == 1:#Koska ykkönen ei ole alkuluku
    print(str(luku)+" Ei ole alkuluku")
elif luku > 1:
    for i in range(2,luku):#Käy läpi onko luku jaollinen kahdella tai jollakin luvulla syötettyä lukua edeltävään lukuun saakka
        if (luku % i ) == 0:
            print("Luku ei ole alkuluku")
            break
    else:
        print(str(luku)+" on alkuluku")

else:
    print("Luku ei ole alkuluku")
