import random
N = int(input("Syötä pisteiden lukumäärä")) #pisteiden_lukumäärä
n = 0 #ympyrään_osuvat
toistot = N
while toistot > 0:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    laskutoimitus = x**2+y**2
    toistot = toistot - 1
    if float(laskutoimitus) < 1:
        n = n + 1
pii = 4 * n/N
print("Tässä on piin likiarvo "+ str(pii))