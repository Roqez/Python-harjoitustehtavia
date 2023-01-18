isoin = 0
pienin = None
luku = None

while True:
    luku = input("Syötä lukuja")
    if luku =='':
        break
    if pienin == None:
        pienin = float(luku)
    if float(luku) > (isoin):
        isoin = float(luku)
    if float(luku) < pienin:
        pienin = float(luku)

print("Isoin luku on "+str(isoin)+" ja pienin luku on "+str(pienin))
