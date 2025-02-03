luku = int(input("Anna kokonaisluku: "))

on_alku_luku = True

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        on_alku_luku = False

if on_alku_luku:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")
        