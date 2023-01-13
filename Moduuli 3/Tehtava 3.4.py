vuosi = int(input("Syötä vuosiluku niin kerron onko se karkausvuosi"))
if vuosi%100 == 0 and vuosi%400 == 0:
    print("Vuosi on karkausvuosi")
elif vuosi%4 == 0 and vuosi%100 != 0:
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")
