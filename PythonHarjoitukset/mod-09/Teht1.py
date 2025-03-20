class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettuMatka = 0

auto = Auto("ABC-123", "142 km/h")
print(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettuMatka)