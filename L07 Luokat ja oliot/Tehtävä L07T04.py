#Lab07 Tehtävä 04

# create the class
class Mobile:
    brand = ""
    model = ""
    price = 0

# create a method for creating new objects
    def __init__(self, brand = "", model = "", price = 0):
        self.brand = brand
        self.model = model
        self.price = price

# return the info of each object as a string
    def __str__(self):
        return self.brand + " " + self.model + " on " + str(self.price) + " €"

# create the objects
phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)

# print the objects
print(phone1)
print(phone2)