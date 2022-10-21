#Lab06 Tehtävä 04

# request the points per jump
def hyppy_pisteet():
    pisteet_yhteensa = []
    for x in range(5):
        luku = int(input("Hypyn pisteet: "))
        pisteet_yhteensa.append(luku)

# remove the lowest and highest score
    pisteet_yhteensa.sort()
    pisteet_yhteensa.pop(0)
    pisteet_yhteensa.pop(-1)
    kaiket_pisteet = sum(pisteet_yhteensa)
    print(f"Pisteet yhteensä: {kaiket_pisteet}")

# carry out the program
hyppy_pisteet()
