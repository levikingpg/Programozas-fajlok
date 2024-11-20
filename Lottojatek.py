#szamok sorsolasa ( 1- 90 ), nincs ismetlodes
#felhasznalotol bekerni szamokat, nincs ismetlodes, csak a tartomanyba irhat
#talalatok szama
#mennyi a nyeremenye
nums = []
helytal = 0
import random
for i in range(5):
    szam = random.randint(1, 90)
    if szam not in nums:
        nums.append(szam)

tippek = []
for i in range(5):
    eszam = int(input("Írd be a tippjeidet bro:"))
    tippek.append(eszam)

print(tippek)








print(f"neked {helytal} helyes talalatod van")


