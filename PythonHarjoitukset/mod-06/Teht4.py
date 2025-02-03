def listanSumma(lista):
    lista_summa = 0
    for item in lista:
        lista_summa += item
    return lista_summa

print("Luo lista antamalla numeroita, ohjelma pysähtyy kun syötät tyhjän merkkijonon.")

klista = []

while True:
    luku = input("Anna luku: ")
    if luku != "":
        klista.append(int(luku))
    else:
        print(f"Lukujen summa on {listanSumma(klista)}")
        break
