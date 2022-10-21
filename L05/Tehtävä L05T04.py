#Lab05 Tehtävä 04

#funktio laskee automatkan kokonaiskulutus
def get_fuel(ajettu_km,keskikulutus):
    kulutus = keskikulutus / 100 * ajettu_km
    print(f"{kulutus:.1f} ltr")

#kutsutaan funktiota
print(get_fuel(100,7.5))
print(get_fuel(220,6.9))