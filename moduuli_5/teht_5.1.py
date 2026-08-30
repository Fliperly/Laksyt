import random
määra = int(input("Anna arpakuutioiden määrä: "))

summa = 0
for i in range(määra):
    heitto = random.randint(1, 6)
    summa = summa + heitto

print("Silmälukujen summa:", summa)