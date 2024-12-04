    f = open("sziget.txt" , "r" , encoding="utf-8")
sorok = f.readlines()
f.close()

print(sorok)
meresek = []

for i in range(len(sorok)):
    meresek.append(int(sorok[i].strip()))

print(meresek)

#csa levi bakazs?