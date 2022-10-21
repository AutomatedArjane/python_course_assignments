#Lab05 Tehtävä 05

#funktio laskee automatkan kokonaishinta
def get_cost(ajettu_km, keskikulutus, hinta):
    kokonaishinta = (ajettu_km / 100) * keskikulutus * hinta
    print(f"{kokonaishinta:.2f} €")

#kutsutaan funktiota
print(get_cost(100,7.5,1.88))
print(get_cost(220,6.9,1.88))