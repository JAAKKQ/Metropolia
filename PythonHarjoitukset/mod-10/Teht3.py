class Hissi:
    def __init__(self, alin, ylin, id=0):
        self.id = id
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.nykyinen_kerros = alin

    def ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi {self.id} on nyt {self.nykyinen_kerros} kerroksessa")

    def alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi {self.id} on nyt {self.nykyinen_kerros} kerroksessa")


    def siirry_kerrokseen(self, kerros=None):
        if not kerros:
            kerros = self.alin_kerros
        while self.nykyinen_kerros < kerros and kerros <= self.ylin_kerros:
            self.ylös()
        while self.nykyinen_kerros > kerros and kerros >= self.alin_kerros:
            self.alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = []
        for i in range(hissien_lukumaara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros, i))

    def aja_hissiä(self, hissi, kerros):
        self.hissit[hissi].siirry_kerrokseen(kerros)

    def palohälytys(self):
        for i, hissi in enumerate(self.hissit):
            hissi.siirry_kerrokseen()

talo = Talo(1, 32, 5)

talo.aja_hissiä(0,7)

talo.aja_hissiä(1,4)

print("Palohälytys")
talo.palohälytys()