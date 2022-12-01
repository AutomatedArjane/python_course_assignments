#Lab07 Tehtävä 01

# create the class
class Pelikortti:
    maa = ""
    arvo = 0

# create the playing cards
kortti1 = Pelikortti()
kortti1.maa = "hertta"
kortti1.arvo = 3

kortti2 = Pelikortti()
kortti2.maa = "ruutu"
kortti2.arvo = 12

kortti3 = Pelikortti()
kortti3.maa = "risti"
kortti3.arvo = 3

kortti4 = Pelikortti()
kortti4.maa = "pata"
kortti4.arvo = 8

kortti5 = Pelikortti()
kortti5.maa = "hertta"
kortti5.arvo = 14

# print the playing cards
print(kortti1.maa, kortti1.arvo)
print(kortti2.maa, kortti2.arvo)
print(kortti3.maa, kortti3.arvo)
print(kortti4.maa, kortti4.arvo)
print(kortti5.maa, kortti5.arvo)