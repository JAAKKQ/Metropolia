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

autot = []

for i in range(10):
    auto = Auto(f"ABC-{i+1}", random.randint(100,200))
    auto.kiihdytä(random.randint(-10, 15))
    auto.kulje(1)
    autot.append(auto)


voittaja_auto = None

while not voittaja_auto:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            voittaja_auto = auto
            break
        
autot.sort(key=lambda x: x.kuljettu_matka, reverse=True)
print(f"{"Sijoitus":<15} {"Rekisteritunnus":<20} {"Huippunopeus":<20} {"Nopeus":<15} {"Kuljettumatka":<20}")
print("-"*75)
for i, auto in enumerate(autot):
    print(f"{i+1:<15} {auto.rekisteritunnus:<20} {str(auto.huippunopeus) +" km/h":<20} {str(auto.nopeus) + " km/h":<15} {str(auto.kuljettu_matka) + " km":<20}")