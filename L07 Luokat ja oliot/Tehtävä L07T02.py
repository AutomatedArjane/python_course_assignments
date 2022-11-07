#Lab07 Tehtävä 02

# create the class
class Human:
    name = ""
    age = 0

# return the info of each object as a string
    def __str__(self):
        return "Nimi: " + self.name + ", ikä: " + str(self.age)

# create two objects
human1 = Human()
human1.name = "Adam"
human1.age = 19

human2 = Human()
human2.name = "Eva"
human2.age = 18

# print the objects
print(human1)
print(human2)