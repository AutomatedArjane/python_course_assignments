#Lab02 Tehtävä 03 

# split first and last name into two strings and print them seperately
nimi = input("Anna nimesi: ")
etunimen_loppu = nimi.find(' ')
sukunimen_loppu = len(nimi)
etunimi = nimi[0:etunimen_loppu]
sukunimi = nimi[etunimen_loppu+1:sukunimen_loppu]
print(etunimi)
print(sukunimi)