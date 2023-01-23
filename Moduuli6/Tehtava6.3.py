def gallonan_muunto(gallona):
    litra = gallona * 3.785
    return litra


gallona = int(input("Syötä bensiinimäärä gallonissa niin muutan ne litroiksi"))
while gallona > 0:
    gallonan_muunto(gallona)
    tulos = gallonan_muunto(gallona)
    print(str(gallona)+" Gallonaa muunnetuna litroiksi on : "+str(tulos)+" gallonaa.")
    gallona = int(input("Syötä bensiinimäärä gallonissa niin muutan ne litroiksi"))
print("Kiitos ohjelman käytöstä")