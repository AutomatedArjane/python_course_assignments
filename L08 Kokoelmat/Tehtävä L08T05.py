#Lab08 Tehtävä 05

# import the random module
import random

# create a list for the lotto numbers
lotto_number = []

# create the function
def lotto():
    while len(lotto_number) < 7:
        new_number = random.randint(1,40)
        if new_number not in lotto_number:
            lotto_number.append(new_number) # generate 7 random numbers

    lotto_number.sort() # sort the numbers

    print(*lotto_number, sep = ", ") # print the list items, split by a comma

# carry out the function
lotto()