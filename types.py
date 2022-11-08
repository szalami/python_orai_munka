print("alma")   #string
print(45)       #egesz
print(45.0)     #valós
print(True)     #boolean /igaz - hamis/
print(False)    #boolean /igaz - hamis/

# változók

szam = 45
print("A szam változó:", szam)
szam = 65
print("A megváltozott szam változó:", szam)

print(type(szam))       # int   = egész
print(type(45.2))       # float = lebegőpontos
print(type(0.452E+2))   # float = lebegőpontos /tudományos alak/
print(type("alma"))     # str   = szöveg
print(type(True))       # bool  = boolean

szam = 45
eredmeny = szam + 3     # kifejezés = 1 vagy több változó vagy állandó és 1 operáto /műveleti jel/
                        # az a = jel -> értékadó operátor 
szo1 = "alma"
szo2 = "körte"
mondat = szo1 + " " + szo2  
print(mondat)

szam2 = float(5)        # megváltoztatom a típusát a float függvénnyel
print(type(szam2))

# Literális állandó

szam3 = 3_000_000       # a jobban olvashatóság miatt
print("A szam3 típusa:", type(szam3))

mondat1 = "I'm"
mondat2 = 'I am'        # aposztrófok közé nem lehet aposztrófot rakni
                        # csak így 'I\'m'
mondat3 = '"alma"'      # így megjelenik az idézőjel
print(mondat1, mondat2, mondat3)

#formázott kimenet

num = 38
print("{:10}".format(num))          # tíz helyes behúzást csinál
print("{:>10}".format("alma"))      # tíz helyes behúzást csinál, a szövegnél kell a ">" a jobbra toláshoz
print("|{:<10}|".format(48))        # tíz helyes behúzást csinál balra
print("|{:^10}|".format(48))        # középre igazít

print("|{:_<10}|".format(48))       # kitölti a maradék helyet az adott karakterrel most:"_"
print("|{:10.2f}|".format(48.123456789)) #csak két tizedes jeggyel jelenik meg 10 karakter szélességben
print("|{:10.2f} kg|".format(48.123456789)) #kap pl egy mértékegységet /formátum string/
print("|{:10.2f} kg {} Ft|".format(48.123456789, 375)) #kap az első szám pl egy mértékegységet /formátum string/, a másik szám egy másikat /Ft/


# modulo formázás

print("%20d" % 48)                  # 20 karakter behúzás
print("%20d %10.2f" % (48, 456.5))  # 20 karakter behúzás az egész számnak /d/ és tíz helyes a floatnak /f/ két tizedes jegyig
print("%20d %10.2f %10s" % (48, 456.5, "alma"))  # 20 karakter behúzás az egész számnak /d/ és tíz helyes a floatnak /f/ két tizedes jegyig, aszöveg formázásához -> s
                                    # a számok helyett változó is lehet

# matek

# hatvány
print(pow(2, 8))    # 2 a 8.-on
print(2**8)         # ugyanaz
print(5/2)          # valós osztás
print(5//2)         # egész osztás
print(5%2)          # maradékot adja vissza

















