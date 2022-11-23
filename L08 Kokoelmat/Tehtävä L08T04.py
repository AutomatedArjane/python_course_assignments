#Lab08 Tehtävä 04

# create the list
cars_list = {}

# ask for license plates and brands and add them to the dictionary.
for x in range (0,10):
    license_plate = input("Anna rekisterinumerosi: ")
    brand = input("Anna autonmerkki: ")
    cars_list[license_plate] = brand

# sort keys of dictionary
sorted_cars = dict(sorted(cars_list.items()))

# print the sorted keys and values
for key, value in sorted_cars.items():
    print(key, value)