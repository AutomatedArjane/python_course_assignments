#Lab07 Tehtävä 03

# create the class
class Cat:
    name = ""
    color = ""

# return the info of each object as a string
    def __str__(self):
        return self.name + ", color: " + self.color

# make the cats miau
    def naukumaan(self):
        print(self.name + " says: Meoooooow!")

# create the objects
cat1 = Cat()
cat1.name = "Kit"
cat1.color = "black"

cat2 = Cat()
cat2.name = "Kat"
cat2.color = "white"

# print the objects
print(cat1)
print(cat2)

Cat.naukumaan(cat1)
Cat.naukumaan(cat2)

