# Lab06 Tehtävä 02

# a function to convert Celsius to Fahrenheit
def celToFah(temp_in_C):
    Fahrenheit = float((temp_in_C * 1.8) + 32)
    print(f"{Fahrenheit:.1f}")

# a function to convert Fahrenheit to Celsius
def fahToCel(temp_in_F):
    Celsius = (temp_in_F - 32) * (5 / 9)
    print(f"{Celsius:.1f}")

# test the function
print(celToFah(10.0))
print(fahToCel(38.0))