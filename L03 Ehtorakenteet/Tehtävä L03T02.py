#Lab03 Tehtävä 02 
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

# print the biggest given number
if luku1 > luku2 and luku1 > luku3:
    print(f"Suurin: {luku1}")
elif luku2 > luku1 and luku2 > luku3:
    print(f"Suurin: {luku2}")
else:
    print(f"Suurin: {luku3}")