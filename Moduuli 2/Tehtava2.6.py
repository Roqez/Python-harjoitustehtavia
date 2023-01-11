import random
eka = str(random.randint (0,9))
toka = str(random.randint (0,9))
kolmas = str(random.randint (0,9))
neljäs = str(random.randint (1,6))
viides = str(random.randint (1,6))
kuudes = str(random.randint (1,6))
seitsemäs = str(random.randint (1,6))
koodi1 = eka+toka+kolmas
koodi2 = neljäs+viides+kuudes+seitsemäs
print("Tässä on ensimmäisen lukon koodi "+str(koodi1)+" Tässä on toisen lukon koodi "+str(koodi2))