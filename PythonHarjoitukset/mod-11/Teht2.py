class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
    
    def kiihdytä(self, lisäys):
        uusi_nopeus = self.nopeus + lisäys
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus
    
    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nopeus * tuntimäärä

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko

sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttoauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(100)
polttoauto.kiihdytä(90)  

sahkoauto.kulje(3)
polttoauto.kulje(3)

print(f"Sähköauto {sahkoauto.rekisteritunnus} on ajanut {sahkoauto.kuljettu_matka} km.")
print(f"Polttomoottoriauto {polttoauto.rekisteritunnus} on ajanut {polttoauto.kuljettu_matka} km.")
