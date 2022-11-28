#Lab09 Tehtävä 03

# create the file name and a numbers list
filename = "luvut.txt"
numbers_list = []

# throw an exception if file opening fails
try:
    file = open(filename, "w")
except:
    print(f"Tiedoston {filename} avaaminen epäonnistui")

while True:
    integer = input("Anna luku: ")

    if integer != "":
        numbers_list.append(integer)
    
    else:
        break

# write each number in the file
for number in numbers_list:
    file.write(number + "\n")

# write the total number of integers into the file
file.write(f"Syötetty {len(numbers_list)} lukua.")

# close the file
file.close()