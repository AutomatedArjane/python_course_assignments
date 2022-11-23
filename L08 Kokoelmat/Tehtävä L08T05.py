#Lab08 Tehtävä 05

# import the random module
import random

# create a list for the lotto numbers
lotto_number = []

# create the function
def lotto():
    for x in range(0,7):
        lotto_number.append(random.randint(1,40)) # generate 7 random numbers

    lotto_number.sort() # sort the numbers

    print(*lotto_number, sep = ", ") # print the list items, split by a comma

# carry out the function
lotto()