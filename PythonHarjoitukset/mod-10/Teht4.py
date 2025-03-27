import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
        self.kello = 0
    
    def kiihdytä(self, nopeus):
        uusiNopeus = self.nopeus + nopeus
        if uusiNopeus < self.huippunopeus and uusiNopeus > 0:
            self.nopeus = uusiNopeus
        elif uusiNopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusiNopeus < 0:
            self.nopeus = 0
    
    def kulje(self, tuntiMaara):
        self.kuljettu_matka += self.nopeus * tuntiMaara

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    
    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)
    
    def tulosta_tilanne(self):
        self.autot.sort(key=lambda x: x.kuljettu_matka, reverse=True)
        print(f"{'Sijoitus':<10} {'Rekisteri':<15} {'Huippunopeus':<20} {'Nopeus':<15} {'Matka (km)':<15}")
        print("-" * 75)
        for i, auto in enumerate(self.autot, 1):
            print(f"{i:<10} {auto.rekisteritunnus:<15} {auto.huippunopeus:<20} {auto.nopeus:<15} {auto.kuljettu_matka:<15}")
        print()
    
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
    
tunti = 0
while True:
    kilpailu.tunti_kuluu()
    tunti += 1
    
    if tunti % 10 == 0:
        print(f"\nTilanne {tunti} tunnin jälkeen:")
        kilpailu.tulosta_tilanne()
    
    if kilpailu.kilpailu_ohi():
        print("Kilpailu on päättynyt! Lopputilanne:")
        kilpailu.tulosta_tilanne()
        break