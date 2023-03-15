class Hissi:
    def __init__(self,alinkerros,ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerrosnyt = 0

    def kerros_ylös(self,kerrosnyt,ylinkerros):
        if kerrosnyt + 1 <= ylinkerros:
            self.kerrosnyt = kerrosnyt + 1
        else:
            print("Olet jo ylimmässä kerroksessa")
    def kerros_alas(self,kerrosnyt,alinkerros):
        if kerrosnyt - 1 >= alinkerros:
            self.kerrosnyt = kerrosnyt - 1
        else:
            print("Olet jo alimmassa kerroksessa")

    def siirry_kerrokseen(self,alinkerros,ylinkerros,haluttukerros):
        if haluttukerros >= alinkerros and haluttukerros <= ylinkerros:
            self.kerrosnyt = haluttukerros
        else:
            print("Virheellinen kerros")

