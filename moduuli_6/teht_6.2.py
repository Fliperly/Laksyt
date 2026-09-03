import random
def heita_noppaa(tahkot):
    silmaluku = random.randint(1, tahkot)
    return silmaluku

noppa = 0
maksimi = int(input("Anna nopan tahkojen määrä: "))

while noppa != maksimi:
    noppa = heita_noppaa(maksimi)
    print(noppa)