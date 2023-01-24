def summaus(luvut):
    for i in luvut:
        if i%2 == 0:
            uusi_lista.append(i)
    return uusi_lista


uusi_lista = []
luvut = [1,2,5,8,9,101,550,333]
print(luvut)
print(summaus(luvut))