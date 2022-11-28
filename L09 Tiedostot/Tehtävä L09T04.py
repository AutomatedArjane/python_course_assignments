#Lab09 Tehtävä 04

# set file name and create dictionary
filename = "nimet.txt"
names_dict = {}

# throw an exception if file opening fails
try:
    file = open(filename, "r")
except:
    print(f"Tiedoston {filename} avaaminen epäonnistui")

# go through the names one by one. Add 1 to the number of names (= dictionary value) every time it is found.
for name in file:
    if name in names_dict:
        names_dict[name] += 1
    else:
        names_dict[name] = 1

# print how many names are in the list
print(f"\nTiedostossa '{filename}' ovat {len(names_dict)} nimiä.\n")

# print each name and how often they occur in the list
for key, value in names_dict.items():
    key = key.strip()
    print(f"{key}: {value}x")

# close the file
file.close()