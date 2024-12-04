f = open("03_000.txt" , "r" , encoding="utf-8")
sorok = f.readlines()
f. close()

szamok = []
for i in range(len(sorok)):
    szamok.append(int(sorok[i]))

print(szamok)

van = False

for i in range(len(szamok)):
    if szamok[i] % 100 == 0:
        van = True
    break

if van == True:
    print("VAn 100al oszthato szam")

else:
    print("NInccs 100 al oszthato szam")

#2. feladat
for i in reversed(range(len(szamok))):
    if szamok[i] % 7 == 0:
        print(f"Azu utolso 7tel oszthato szam indexe {i}")
        break

#3. feladat
for i in range(len(szamok)):
    if szamok[i] % 19 == 0:
        print(f"Az elso 19 el oszthato szam  indexe :{i}")
        break

#4. feladat
osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]

atlag = osszeg / len(szamok)

print(f"a szamok atlaganak negyzete: {atlag ** 2}")

#5. feladat
nagyobb10 = True
for i in range(len(szamok)):
    if szamok[i] <= 10:
        nagyobb10 = False
        break
if nagyobb10 == True:
    print("Mindegyik nagyobb mint 10")
else:
    print("Mindegyik kisseb mint 10")

#6. feladat

db =   0
for i in range(len(szamok)):
    if szamok[i] % 9 == 0:
        db += 1
    break
print(f"{db} 9cel oszthato szam van")

#7. fel
for i in range(len(szamok)):
    if szamok[i] % 15 == 0:
        print(szamok[i] / 2)

#9 fel
van = False
for i in range(len(szamok) -1 ):
    if szamok[i] < 0 and szamok[i + 1] > 0:
        van = True
        break

if van == True:
    print("VAn olyan negativ szam amit egy pozitiv kovet")

else:
    print("Nincs olyan negativ szam amit egy pozitiv kovet")


#10. feladat
min = szamok[0]
for i in range(len(szamok)):
    if szamok[i] < min:
        min = szamok[i]

print(f"A legkisebb szam fele : {min / 2}")

#11. feladat
pozitiv = open("pozitiv.txt" , "w" , encoding="utf-8")
negativ = open("negativ.txt" , "w" , encoding="utf-8")

for i in range(len(szamok)):
    if szamok[i] <  0:
        print(szamok[i] , file=negativ)
    else:
        print(szamok[i] , file=pozitiv)


pozitiv.close()
negativ.close()
