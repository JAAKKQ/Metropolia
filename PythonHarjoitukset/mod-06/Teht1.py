import random

def noppa():
    return random.randint(1,6)

while True:
    tulos = noppa()
    print(tulos)
    if tulos == 6:
        break