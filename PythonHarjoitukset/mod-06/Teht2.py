import random

luku = int(input("Anna nopan tahkojen lukumäärä: "))

def noppa(tahkoja):
    return random.randint(1,tahkoja)

while True:
    tulos = noppa(luku)
    print(tulos)
    if tulos == luku:
        break