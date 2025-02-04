import random

pisteet_ympyran_sisalla = 0
kaikki_pisteet = int(input("Anna pisteiden määrä: "))

for i in range(kaikki_pisteet):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        pisteet_ympyran_sisalla += 1

print(f"Piin likiarvo on {4*pisteet_ympyran_sisalla/kaikki_pisteet}")