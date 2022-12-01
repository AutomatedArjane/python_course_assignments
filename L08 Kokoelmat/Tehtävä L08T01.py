#Lab08 Tehtävä 01

# create the list
name_list = []

# ask for 10 names and add each name to the list
for x in range (0,10):
    friend_name = input("Anna kaverin nimi: ")
    name_list.append(friend_name)

# reverse the order of the list
name_list.reverse()

# print each name of the list
for name in name_list:
    print(name)