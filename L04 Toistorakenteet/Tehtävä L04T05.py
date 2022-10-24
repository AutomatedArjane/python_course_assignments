#Lab04 Tehtävä 05
etunimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")
lasku = len(sukunimi) - 1

# print first letter of first name x times
for x in range(len(etunimi)):
    print(etunimi[0])

# print last name in reverse
for y in range(len(sukunimi)):
    print(sukunimi[lasku])
    lasku -= 1