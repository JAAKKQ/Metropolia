kerta = 0

while True:
    if kerta > 5:
        break
    kayttaja = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if salasana == "rules" and kayttaja == "python":
        print("Tervetuloa")
        break
    else:
        kerta+=1
        print("Pääsy evätty")

