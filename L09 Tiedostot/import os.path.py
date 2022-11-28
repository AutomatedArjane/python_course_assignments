import os.path
nimet = ["Allu", "Bella", "Calle"]
polku = os.path.expanduser("~")
tiedosto = "testi251122.txt"
tiedosto2 = polku + "/"+ tiedosto
file = open(tiedosto2 , "w")
for nimi in nimet:
    file.write(nimi + "\n")
file.close()
print(tiedosto2 + " luotu onnistuneesti.")