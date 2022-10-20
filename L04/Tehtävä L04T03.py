#Lab04 Tehtävä 03
annettu = 0
summa = 0

while True:
    luku = input("Anna luku: ")

    if luku == "":
        print(f"lukujen annettu: {annettu}")
        print(f"Lukujen summa: {summa}")
        break
    else:
        annettu += 1
        summa += int(luku)
        continue