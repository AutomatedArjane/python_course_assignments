#Lab08 Tehtävä 05

# import the random module
import random

# create a list for the lotto numbers
lotto_number = []

# create the function
def lotto():
    printable_lotto_number = ""
    
    while len(lotto_number) < 7:
        new_number = random.randint(1,40)
        if new_number not in lotto_number:
            lotto_number.append(new_number) # generate 7 random numbers

    lotto_number.sort() # sort the numbers

    for number in lotto_number:
        printable_lotto_number += str(number) + ", "
        
    print(printable_lotto_number[0:-2])

# carry out the function
lotto()