#Lab06 Tehtävä 04

# request the points per jump
def hyppy_pisteet():
    pisteet_yhteensa = 0
    isoin = 0
    pienin = 20
    laskuri = 1

    while laskuri <= 5:
        luku = int(input("Hypyn pisteet: "))
        if luku >= 1 and luku <= 20:
            pisteet_yhteensa += luku
            laskuri += 1
        else:
            continue

        # determine the highest and lowest score, and remove them from the total score
        if luku > isoin:
            isoin = luku
        elif luku < pienin:
            pienin = luku
    pisteet_yhteensa = pisteet_yhteensa - isoin - pienin

    print(f"Pisteet yhteensä: {pisteet_yhteensa}")

# carry out the program
hyppy_pisteet()