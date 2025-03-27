class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print("Nimi:", self.nimi)

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}\nKirjailija: {self.kirjoittaja}\nSivumäärä: {self.sivumaara}\n")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}\nPäätoimittaja: {self.paatoimittaja}\n")

# Pääohjelma
aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_no6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti_no6.tulosta_tiedot()
