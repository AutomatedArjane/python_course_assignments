#Lab09 Tehtävä 01

# create the file and a name list
filename = "names.txt"
surname_list = []

# throw an exception if file opening fails
try:
    file = open(filename, "w")
except:
    print(f"Tiedoston {filename} avaaminen epäonnistui")

# ask for names until input is empty
while True:        
    surname = input("Anna sukunimesi: ")

    if surname != "":
        surname_list.append(surname)    

    else:
        break

# write each name from the list in the file
for name in surname_list:
    file.write(name + "\n")

# close the file
file.close()