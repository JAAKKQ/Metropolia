def parilliset(lista):
    pariton_lista = []
    for item in lista:
        if item % 2 == 0:
            pariton_lista.append(item)
    return pariton_lista

print("Luo lista antamalla numeroita, ohjelma pysähtyy kun syötät tyhjän merkkijonon.")

klista = []

while True:
    luku = input("Anna luku: ")
    if luku != "":
        klista.append(int(luku))
    else:
        print(f"Annetut luvut: {klista}")
        print(f"Annetuista luvuista parilliset: {parilliset(klista)}")
        break
