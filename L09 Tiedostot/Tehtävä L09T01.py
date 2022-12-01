#Lab09 Tehtävä 01

# create the file
filename = "names.txt"

# throw an exception if file opening fails
try:
    file = open(filename, "a")

    # ask for names until input is empty
    while True:        
        surname = input("Anna sukunimesi: ")

        # write each name from the list in the file, stop if input is empty
        if surname != "":
            file.write(surname + "\n")
        
        else:
            break

# throw an exception
except:
    print(f"Tiedoston {filename} avaaminen epäonnistui")

# close the file
finally:
    file.close()