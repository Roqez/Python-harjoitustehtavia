class Hissi:
    def __init__(self,alinkerros,ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerrosnyt = alinkerros
    def kerros_ylös(self,kerrosnyt,ylinkerros):
        if kerrosnyt + 1 <= ylinkerros:
            self.kerrosnyt = kerrosnyt + 1
        else:
            print("Olet jo ylimmässä kerroksessa")
        print("Olet nyt "+str(self.kerrosnyt)+" kerroksessa")
    def kerros_alas(self,kerrosnyt,alinkerros):
        if kerrosnyt - 1 >= alinkerros:
            self.kerrosnyt = kerrosnyt - 1
        else:
            print("Olet jo alimmassa kerroksessa")
        print("Olet nyt "+str(self.kerrosnyt)+" kerroksessa")
    def siirry_kerrokseen(self,haluttukerros):
        if haluttukerros >= self.alinkerros and haluttukerros <= self.ylinkerros:
            if haluttukerros > self.kerrosnyt:
                while self.kerrosnyt < haluttukerros:
                    h.kerros_ylös(self.kerrosnyt,self.ylinkerros)
            else:
                while self.kerrosnyt > haluttukerros:
                    h.kerros_alas(self.kerrosnyt,self.alinkerros)
        else:
            print("Virheellinen kerros")
h = Hissi (0,5)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(0)