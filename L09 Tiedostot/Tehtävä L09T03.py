#Lab09 Tehtävä 03

# create the file name
filename = "luvut.txt"
no_of_integers = 0

# throw an exception if file opening fails
try:
    file = open(filename, "w")

    while True:
        integer = input("Anna luku: ")

        if integer != "": # write each number in the file
            file.write(integer + "\n")
            no_of_integers += 1
        
        else:
            break

    # write the total number of integers into the file
    file.write(f"Syötetty {no_of_integers} lukua.")

# throw an exception
except:
    print(f"Tiedoston {filename} avaaminen epäonnistui")

# close the file
finally:
    file.close()