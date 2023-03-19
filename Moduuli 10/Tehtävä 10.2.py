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
    def kerros_ylös(self):
        if self.kerrosnyt + 1 <= self.ylinkerros:
            self.kerrosnyt = self.kerrosnyt + 1
        else:
            print("Olet jo ylimmässä kerroksessa")
        print("Olet nyt "+str(self.kerrosnyt)+" kerroksessa")
    def kerros_alas(self):
        if self.kerrosnyt - 1 >= self.alinkerros:
            self.kerrosnyt = self.kerrosnyt - 1
        else:
            print("Olet jo alimmassa kerroksessa")
        print("Olet nyt "+str(self.kerrosnyt)+" kerroksessa")
    def siirry_kerrokseen(self,haluttukerros):
            if haluttukerros >= self.alinkerros and haluttukerros <= self.ylinkerros:
                if haluttukerros > self.kerrosnyt:
                    while self.kerrosnyt < haluttukerros:
                        self.kerros_ylös()
                else:
                    while self.kerrosnyt > haluttukerros:
                        self.kerros_alas()
            else:
                print("Virheellinen kerros")

Eka_talo = Talo (0,10,2)
Eka_talo.aja_hissiä(2,6)