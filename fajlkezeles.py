f = open("be.txt" , "r" , encoding="utf-8")
 
a = int(f.readline())
b = int(f.readline())        

f.close()

osszeg = a + b

f = open("Ki.txt", "w", encoding="Utf-8") #+100 aura

print(osszeg, file=f)

f.close()

#paros es paratlan szamok ket fajlba
f = open("szamok.txt", "r" , encoding="utf-8" )
sor = f.readline()
f.close()
print(sor)

darbok = (sor.split())
print(darbok)

szamok = []
for i in range(len(darbok)):
    szamok.append(int(darbok[i]))

print(szamok)

paros = open("paros.txt", "w", encoding="utf-8")
paratlans    = open("paratlans.txt", "w", encoding="utf-8")

for i in range(len(szamok)):
    if szamok[i] % 2 == 0:
        print(szamok[i], file=paros)
else:
    print(szamok[i], file=paratlans)

paros.close()
paratlans.close()