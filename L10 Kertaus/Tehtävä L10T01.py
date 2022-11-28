#Lab10 Tehtävä 01

saldo = 2000 # create the variable
print(f"Bank account balance: {saldo} €") # print the account balance
euros_addition = int(input("How many euros will be added to the balance? ")) # n euro will be added to the balance
cents_addition = int(input("How many cents will be added to the balance? ")) # n cents will be added to the balance
saldo = saldo + euros_addition + (cents_addition/100) # add the euros and cents to the balance
print(f"Bank account balance: {saldo} €") # print the new balance