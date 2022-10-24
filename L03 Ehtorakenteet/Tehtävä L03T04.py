#Lab03 Tehtävä 04 
pisteet = int(input("Pisteet: "))

# calculate the grade based on number of points
if pisteet <= 5:
    if pisteet <= 1:
        print(f"Arvosana: 0")
    elif pisteet <= 3:
        print(f"Arvosana: 1")
    else:
        print(f"Arvosana: 2")
else:
    if pisteet <= 7:
        print(f"Arvosana: 3")
    elif pisteet <= 9:
        print(f"Arvosana: 4")
    else:
        print(f"Arvosana: 5")