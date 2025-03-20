class Hissi:
    def __init__(self, alin, ylin):
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.nykyinen_kerros = alin

    def ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on nyt {self.nykyinen_kerros} kerroksessa")

    def alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on nyt {self.nykyinen_kerros} kerroksessa")


    def siirry_kerrokseen(self, kerros):
        while self.nykyinen_kerros < kerros and kerros <= self.ylin_kerros:
            self.ylös()
        while self.nykyinen_kerros > kerros and kerros >= self.alin_kerros:
            self.alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = []
        for i in range(hissien_lukumaara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissi, kerros):
        self.hissit[hissi].siirry_kerrokseen(kerros)

talo = Talo(1, 32, 5)

print("Hissi 0:")
talo.aja_hissiä(0,7)

print("Hissi 1:")
talo.aja_hissiä(1,4)