#Lab04 Tehtävä 05
etunimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")
lasku = len(sukunimi) - 1

for x in range(len(etunimi)):
    print(etunimi[0])

for y in range(len(sukunimi)):
    print(sukunimi[lasku])
    lasku -= 1