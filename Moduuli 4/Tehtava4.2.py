tuumat = float(input("Anna tuumat niin muutan ne senttimetreiksi"))
sentit = tuumat * 2.54
print(f"{sentit:4.2f} senttimetriä")
while tuumat > 0 :
    tuumat = float(input("Anna tuumat niin muutan ne senttimetreiksi"))
    if tuumat > 0:
        sentit = tuumat * 2.54
        print(f"{sentit:4.2f} senttimetriä")

