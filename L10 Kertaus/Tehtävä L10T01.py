#Lab10 Tehtävä 01

# create the bank account variable
saldo = 2000
print(f"Bank account balance: {saldo} €") # print the account balance

# add money to the bank account
euros_addition = int(input("How many euros will be added to the balance? ")) # n euro will be added to the balance
cents_addition = int(input("How many cents will be added to the balance? ")) # n cents will be added to the balance

# add the euros and cents to the balance
saldo = saldo + euros_addition + (cents_addition/100)
print(f"Bank account balance: {saldo} €") # print the new balance