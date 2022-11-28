#Lab10 Tehtävä 05

# import os.path in order to direct the location of the file we'll create
import os.path

# determine the number of colours in a colour list
colour_number = int(input("How many colours do you want? "))
rainbow = []

# create the list of colours
for x in range(1,colour_number + 1):
    colour = input(f"Enter your favourite colour no. {x}: ")
    rainbow.append(colour)

# determine the file location and create the file
path = os.path.expanduser("~")
filename = "ayho.txt"
filename2 = path + "/"+ filename

# open the file for writing, error handling is included
try:
    file = open(filename2 , "w")
except:
    print(f'Could not open file "{filename}"')

# write the list of colours into the file
for shade in rainbow:
    file.write(shade + "\n")

# close the file
file.close()