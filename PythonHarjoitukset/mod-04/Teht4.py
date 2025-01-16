import random

numero = random.randrange(1,10)

while True:
    arvaus = int(input("Arvaa numero 1-10: "))
    if arvaus == numero:
        print("Oikein")
        break
    if arvaus > numero:
        print("Liian suuri arvaus")
    if arvaus < numero:
        print("Liian pieni arvaus")