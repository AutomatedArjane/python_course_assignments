#Lab08 Tehtävä 02

# create the list
license_plate_list = []

# ask for license plates and add each one to the list. An empty entry stops the loop.
while True:
    license_plate = input("Anna rekisterinumerosi: ")
    if license_plate != "":
        license_plate_list.append(license_plate)
    else:
        break

# sort the list
license_plate_list.sort()

# print each name of the list
for number in license_plate_list:
    print(number)