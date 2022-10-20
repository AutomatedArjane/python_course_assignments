#Lab04 Tehtävä 04
luku = int(input("Anna numero väliltä 1-10: "))

for x in range(luku):
    nelio = (x + 1) ** 2
    print(f"Luvun {x + 1} neliö on {nelio}")