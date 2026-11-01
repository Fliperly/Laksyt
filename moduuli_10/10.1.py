class Hissi:

    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
    self.kerros += 1
    print(f"YLÖS => {self.kerros}")

    def kerros alas(self):
    self.kerros -= 1
    print(f"ALAS => {self.kerros}")

    def siirry_kerrokseen (self, kerros):
        while self.kerros < kerros:
            self.kerros_ylös()
        while self.kerros > kerros:
            self.kerros_alas()




