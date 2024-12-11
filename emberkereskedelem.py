#emberek adatainak tárolása

class ember:
    def __init__(self, nev, szulev , magassag , nem , szin):
        self.nev = nev
        self.szulev = int(szulev)
        self.magassag = int(magassag)
        self.nem = nem
        self.szin = szin
        
kecso = ember("Kecső Máté", 2009, 187, "férfi" , "kek")


adatok = input("Írja be egy ember(vagy robot) adatait:")
darabok = adatok.split(";")
e = ember(darabok[0] , darabok[1] , darabok[2], darabok[3], darabok[4])
print(e.nev)
print(e.szin)

if kecso.magassag > e.magassag:
    print("xy magasabb")
else:
    print(f"{e.nev} magasabb" )

