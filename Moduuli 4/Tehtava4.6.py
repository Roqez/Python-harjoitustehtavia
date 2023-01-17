import random
N = int(input("Syötä pisteiden lukumäärä")) #pisteiden_lukumäärä
n = 0 #ympyrään_osuvat
toistot = N
while toistot > 0:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print("X arvo on"+ str(x))
    print("Y arvo on" + str(y))
    laskutoimitus = x**2+y**2
    print(laskutoimitus)
    toistot = toistot - 1
    print(N)
    if float(laskutoimitus) < 1:
        n = n + 1
pii = 4 * n/N
print("Osumat ympyrään "+ str(n))
print("Tässä on piin likiarvo "+ str(pii))