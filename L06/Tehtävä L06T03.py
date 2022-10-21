#Lab06 Tehtävä 03

# add names to a string
def names():
    paljonko_oppilaita = 0
    nimeja = ""

    while True:
        nimi = input("Anna oppilaan nimi: ")

# check if the imput is empty
        if nimi != "":
            paljonko_oppilaita += 1
            nimeja += nimi + ", "

# remove comma and space from the end of the string, print the results        
        else:
            print(f"Oppilaita: {paljonko_oppilaita}")
            print(nimeja[0:-2])


# carry out the program
names()