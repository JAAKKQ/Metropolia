lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - Lisää uusi lentoasema")
    print("2 - Hae lentoaseman nimi")
    print("3 - Lopeta")
    toiminto = input("Syötä valinta (1-3): ").strip()

    if toiminto == "1":
        icao = input("Syötä lentoaseman ICAO-koodi: ").strip().upper()
        nimi = input("Syötä lentoaseman nimi: ").strip()
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} (ICAO: {icao}) lisätty.")

    elif toiminto == "2":
        icao = input("Syötä haettava ICAO-koodi: ").strip().upper()
        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löydy tietokannasta.")

    elif toiminto == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")