#Lab10 Tehtävä 02

# create the function
def kerro3(age):
    if age < 13:
        return "child"
    elif age >= 13 and age <= 19:
        return "teen"
    elif age >= 20 and age <= 65:
        return "adult"
    else:
        return "senior"

# feed different values to the function to test it
print(kerro3(10))
print(kerro3(13))
print(kerro3(20))
print(kerro3(80))