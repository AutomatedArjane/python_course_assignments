#Lab09 Tehtävä 05

# import the random number generator
import random

# set file name and create a list for the lotto number
filename = "lotto.txt"
lotto_number = []

# throw an exception if file opening fails
try:
    file = open(filename, "w")
except:
    print(f"Tiedoston {filename} avaaminen epäonnistui")

# draw the number of lotto lines the user wants
lotto_lines = int(input("Anna lottorivien määrä: "))
for x in range(0,lotto_lines):
    
# generate a lotto number consisting of 7 random and unique numbers
    while len(lotto_number) < 7:
        new_number = random.randint(1,40)
        if new_number not in lotto_number: # make the numbers all unique
            lotto_number.append(new_number)
    lotto_number.sort() # sort the numbers

    for number in lotto_number:
        file.write(str(number) + " ") # write each number in the file
    file.write("\n") # separate the lines with enter
    
    # reset the lotto number
    lotto_number = []

file.close()