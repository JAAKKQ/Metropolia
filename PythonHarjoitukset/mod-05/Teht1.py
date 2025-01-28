import random

arpakuutioita_luku = int(input("Arpakuutioiden lukumäärä: "))
lukujen_summa = 0

for arpa in range(arpakuutioita_luku):
    lukujen_summa += random.randrange(1,6)


print(f"Silmälukujen summa on {lukujen_summa}")