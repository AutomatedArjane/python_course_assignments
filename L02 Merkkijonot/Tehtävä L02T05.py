#Lab02 Tehtävä 05 

# print the number of letters of a name, and print the first letter of the name as many times
nimi = input("Anna etunimesi: ")
pituus = len(nimi)
print(f"Nimessäsi {nimi} on {pituus} kirjainta.")
print(nimi[0] * pituus)