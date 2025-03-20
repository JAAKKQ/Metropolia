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
    def __init__(self, nimi, km_pituus, autot):
        self.nimi = nimi
        self.km_pituus = km_pituus
        self.autot = autot
        self.voittaja_auto = None
        while not self.voittaja_auto:
            for auto in autot:
                if auto.kuljettu_matka >= 10000:
                    self.voittaja_auto = auto
                    break
        
    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        self.autot.sort(key=lambda x: x.kuljettu_matka, reverse=True)
        print(f"{"Sijoitus":<15} {"Rekisteritunnus":<20} {"Huippunopeus":<20} {"Nopeus":<15} {"Kuljettumatka":<20}")
        print("-"*75)
        for i, auto in enumerate(self.autot):
            print(f"{i+1:<15} {auto.rekisteritunnus:<20} {str(auto.huippunopeus) +" km/h":<20} {str(auto.nopeus) + " km/h":<15} {str(auto.kuljettu_matka) + " km":<20}")

    def kilpailu_ohi(self):
        if self.voittaja_auto:
            return True
        else:
            return False

autot = []

for i in range(10):
    auto = Auto(f"ABC-{i+1}", random.randint(100,200))
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

while True:
    kilpailu.tunti_kuluu()
    if kilpailu.kilpailu_ohi():
        kilpailu.tulosta_tilanne()




        