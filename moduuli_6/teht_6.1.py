import random
def heita_noppaa():
    silmaluku = random.randint(1,6)
    return silmaluku

noppa = 0

while noppa !=6:
    noppa = heita_noppaa()
    print(noppa)
