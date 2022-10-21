#Lab05 Tehtävä 03

#funktio laskee keskiarvo
def average(luku1, luku2, luku3):
    average_number = round((luku1 + luku2 + luku3) / 3, 1)
    return average_number

#kutsutaan funktiota
print(average(2,4,6))
print(average(5,5,6))