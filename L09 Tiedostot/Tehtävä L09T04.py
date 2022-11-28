#Lab09 Tehtävä 04

# set file name
filename = "nimet.txt"

# throw an exception if file opening fails
try:
    file = open(filename, "r")
except:
    print(f"Tiedoston {filename} avaaminen epäonnistui")
    