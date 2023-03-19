class Talo:
    def __init__(self,alinkerros,ylinkerros,hissienlukumaara):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissienlukumaara = hissienlukumaara
        hissit = []
        self.kerrosnyt = alinkerros
        for i in range(hissienlukumaara):
            numero = i+1
            hissi = Hissi(alinkerros,ylinkerros,numero)
            hissit.append(hissi)
        self.hissit = hissit
    def palohälytys(self):
        for i in self.hissit:
            i.siirry_kerrokseen(self.alinkerros)

    def aja_hissiä(self,numero,haluttukerros):
        for i in self.hissit:
            if i.numero == numero:
                i.siirry_kerrokseen(haluttukerros)

class Hissi:
    def __init__(self,alinkerros,ylinkerros,numero):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerrosnyt = alinkerros
        self.numero = numero
    def kerros_ylös(self,numero):
        if self.kerrosnyt + 1 <= self.ylinkerros:
            self.kerrosnyt = self.kerrosnyt + 1
        else:
            print("Olet jo ylimmässä kerroksessa")
        print("Suunta ylös,"" Hissi numero: "+str(numero)+" on nyt "+str(self.kerrosnyt)+" kerroksessa")
    def kerros_alas(self,numero):
        if self.kerrosnyt - 1 >= self.alinkerros:
            self.kerrosnyt = self.kerrosnyt - 1
        else:
            print("Olet jo alimmassa kerroksessa")
        print("Suunta alas,"" Hissi numero: "+str(numero)+" on nyt "+str(self.kerrosnyt)+" kerroksessa")
    def siirry_kerrokseen(self,haluttukerros):
            if haluttukerros >= self.alinkerros and haluttukerros <= self.ylinkerros:
                if haluttukerros > self.kerrosnyt:
                    while self.kerrosnyt < haluttukerros:
                        self.kerros_ylös(self.numero)
                else:
                    while self.kerrosnyt > haluttukerros:
                        self.kerros_alas(self.numero)
            else:
                print("Virheellinen kerros")

Eka_talo = Talo (0,10,5)
Eka_talo.aja_hissiä(4,10)
Eka_talo.aja_hissiä(1,8)
Eka_talo.aja_hissiä(2,7)
Eka_talo.aja_hissiä(3,6)
Eka_talo.aja_hissiä(5,3)
Eka_talo.palohälytys()