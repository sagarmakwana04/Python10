# Python program to find freqency of characters, numerics, spaces, specials, uppers and lowers
s="Python Programming @10:00 am.!!!"

ch=0
nm=0
spc=0
spl=0
up=0
lw=0

for i in s:
    if i.isalpha():
        ch+=1
    elif i.isnumeric():
        nm+=1
    elif i.isspace():
        spc+=1
    else:               # hence, we dont have any built in funcion to check for special so will use it in else block so all are done then rest of char will be special char
        spl+=1
    if i.isupper():
        up+=1
    if i.islower():
        lw+=1

print("Total Length : ",len(s))
print(f"Characters : {ch}")
print(f"Numerics : {nm}")
print(f"Spaces : {spc}")
print(f"Special : {spl}")
print(f"Upper : {up}")
print(f"Lower : {lw}")