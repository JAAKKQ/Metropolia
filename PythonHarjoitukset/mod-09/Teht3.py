class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettuMatka = 0
    
    def kiihdytä(self, nopeus):
        uusiNopeus = self.nopeus + nopeus
        if uusiNopeus < self.huippunopeus and uusiNopeus > 0:
            self.nopeus = uusiNopeus
        elif uusiNopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusiNopeus < 0:
            self.nopeus = 0
    
    def kulje(self, tuntiMaara):
        self.kuljettuMatka = self.nopeus * tuntiMaara

auto = Auto("ABC-123", 142)

print(auto.nopeus)
auto.kiihdytä(60)

auto.kulje(2)
print(auto.kuljettuMatka)