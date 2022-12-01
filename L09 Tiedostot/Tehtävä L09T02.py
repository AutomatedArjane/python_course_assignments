#Lab09 Tehtävä 02

# create the file name and a name list
filename = "names.txt"
names = [""]

# throw an exception if file opening fails
try:
    file = open(filename, "r")
    names = file.readlines() # go through the file line by line

    # print each name from the file, sort alphabetically and print again
    print(names)
    names.sort()
    print(names)

# throw an exception
except:
    print(f"Tiedoston {filename} avaaminen epäonnistui")

# close the file
finally:
    file.close()

