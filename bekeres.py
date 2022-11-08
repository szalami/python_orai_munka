kor = int(input("Add meg a korodat:")) # egész szám /int()/, alapesetben string
nev = input("Add meg neved: ")

print("korod:", kor, "neved:", nev)

# szelekció - feltételek alkalmazása /if - else/

szam = int(input("szám :"))

if szam < 100:
    print("jó")
else:
    print("rossz")

eredmeny = szam < 100
print(type(eredmeny))
print(eredmeny)
