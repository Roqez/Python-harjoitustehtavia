sukupuoli = input("Syötä biologinen sukupuolesi")
arvo = int(input("Syötä hemoglobiini arvosi g/l"))

if arvo < 134 and sukupuoli=="mies":
        print("Hemoglobiini arvosi on alhainen")
elif arvo >= 134 and arvo <= 195 and sukupuoli == "mies":
        print ("Hemoglobiini arvosi on normaali")
elif arvo > 195 and sukupuoli =="mies":
        print("Hemoglobiini arvosi on korkea")
elif arvo < 117 and sukupuoli == "nainen":
        print("Hemoglobiini arvosi on alhainen")
elif arvo >=117 and arvo <= 175 and sukupuoli=="nainen":
        print("Hemoglobiini arvosi on normaali")
elif arvo > 175 and sukupuoli== "nainen":
        print("Hemoglobiini arvosi on korkea")