#Lab04 Tehtävä 02
yhteensa = 0

# print the total amount of rain in a week
for x in range(7):
    sademaara = int(input("Anna sademäärä: "))
    yhteensa += sademaara

print(f"Sademäärä yhteensä: {yhteensa}")