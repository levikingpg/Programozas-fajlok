
import random
szamok = []

for i in range(40):
    szamok.append(random.randint(-50 , 80))

osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]
atlag = osszeg / len(szamok)
print(f"1. feladat: a szamok atlaga: {atlag}")


#2
for i in reversed(range(len(szamok))):
    if szamok[i] % 5 == 0 and szamok[i] % 9 == 0:
        print(f"2. feladat utolso 5tel es 9cel oszthato szamok  index: {i}")
        break


# 3
for i in range(len(szamok)):
    if szamok[i] % 2 == 0 or szamok[i] % 7 == 0:
        print(f"3. feladat utolso 2el vagy 7cel oszthato szamok  szam: {i}")
        break


#4
mindparos = True
for i in range(len(szamok)):
    if szamok[i] % 2 == 1:
        mindparos = False
        break
if mindparos == True:
    print("Mindegyik paros szam")

else:
    print("Nem mindegyik paros szam")

#5
van = False
for i in range(len(szamok)):
    if szamok[i] > 70:
        van = True

if van == True:
    print("Van 70nel nagyobb szam")

else:
    print("Nincs 70nel nagyobb szam.")

#6
db = 0
for i in range(len(szamok)):
    if szamok[i] < 0:
        db += 1

print(f"A sorozat {db} darab negativ szam van")

#7

max = szamok[0]
for i in range(len(szamok)):
    if max == szamok[i] and szamok[i] % 4 == 0:
        max = szamok[i]

print(f"7. feladat legnagyobb 4gyel oszthato szama :  {max}")

#8
db = 0
for i in range(1, len(szamok) - 1):
    if szamok[i] > szamok[i - 1] and szamok[i] > szamok[i + 1]:

print(f" {db} darab lokalis csucs van")

 #11
 pozitiv = []
 negativ = []


 for i in range(len(szamok)) < 0:
    if szamok[i] < 0:
        negativ.append(szamok[i])

    else:
        pozitiv.append(szamok[i])