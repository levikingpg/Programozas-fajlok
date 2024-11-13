import random


szamok = []
for _ in range(30):
    szamok.append(random.randint(-20, 70))
print( szamok)

# 1. feladat:
for i in reversed(range(len(szamok))):
    if szamok[i] % 3 == 0 or szamok[i] % 5 == 0:
        print(f"1. feladat: Az utolsó 3-mal vagy 5-tel oszthaó szam indexe: {i}")
        break

# 2. feladat:
van = False
for szam in szamok:
    if 20 <= szam <= 30:
        van = True
        break
if van:
    print("2. feladat: Van olyan szám, .")
else:
    print("2. feladat: Nincs olyan szám,")

# 3. feladat:
db = 0
for szam in szamok:
    if szam % 7 == 0:
        db += 1
print(f"3. feladat: {db} darab 7-tel osztható szam van a sorozatban.")

# 4. feladat:
max = -21
for szam in szamok:
    if szam < 0:
        if szam > max:
            max= szam
print(f"4. feladat: A legnagyobb negatív szám: {max}")

# 5. feladat:
darab = 0
for i in range(1, len(szamok) - 1):
    elotte = szamok[i - 1]
    utolso = szamok[i + 1]
    if elotte % szamok[i] == 0 and utolso % szamok[i] == 0:
        darab += 1
print(f"5. feladat: {darab} db olyan szam van ami osztolya az elotte es az utana levo szammal is")
