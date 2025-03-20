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

hissi = Hissi(1, 10)

hissi.siirry_kerrokseen(7)
print("-"*30)
hissi.siirry_kerrokseen(1)