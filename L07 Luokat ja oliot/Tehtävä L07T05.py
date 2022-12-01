#Lab07 Tehtävä 05

# create the class
class Car:
    brand = ""
    model = ""
    price = 0

# make a method for creating new objects
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price

    # return the info of each object as a string
    def __str__(self):
        return "auto: " + self.brand + " " + self.model + " " + str(self.price)

# create the objects
car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

# print the objects
print(car1)
print(car2)
print(car3)

summa = car1.price + car2.price + car3.price
print(f"Autojen hinta yhteensä: {summa}")