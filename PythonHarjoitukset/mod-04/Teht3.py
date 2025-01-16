luku = 0
lista = []

while luku != "":
    luku = input("Anna luku: ")
    if luku !="":
        lista.append(int(luku))
print(f"{min(lista)} on pienin luvuista ja {max(lista)} on suurin.")