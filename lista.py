gyumolcsok = ["alma" , "körte" , "Barack","szilva"]
print(gyumolcsok)

gyumolcsok.append("szőlő")
print(gyumolcsok)
print(gyumolcsok[0]) #lista első eleme
print(gyumolcsok[1]) #lista második eleme
print(gyumolcsok[-1]) #lista utolso eleme
print(gyumolcsok[1:4]) #lista 2-4 elemei

gyumolcsok.append(5)
gyumolcsok.append(12)
print(gyumolcsok)

#toltsunk fel egy 50 elemu listat 1 es 100 kozotti veletlen szamokkal!
paros = 0
import random
szamok = [] # ures lista pistalistaa
for i in range(50):
    szamok.append(random.randint (1, 100))

# hany db paros szam van benne

for i in range(len(szamok)):
    if szamok[i] % 2 == 0:
        paros += 1

print(szamok)
print(f"{paros} paros szamunk van")


















































































#zoli snust arul