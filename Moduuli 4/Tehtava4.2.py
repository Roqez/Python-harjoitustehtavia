tuumat = float(input("Anna tuumat niin muutan ne senttimetreiksi"))
sentit = tuumat * 2.54
toisto = 0
while tuumat > 0 and toisto <1:
    print(f"{sentit:4.2f} senttimetriä")
    toisto = toisto +1
