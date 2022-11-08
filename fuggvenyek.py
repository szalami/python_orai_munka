def duplaz(szam):           # ide kerül a paraméter (most pl a 6) 
    eredmeny = szam * 2
    return eredmeny

result = duplaz(6)          # a 6-ot /paramétert átadom a függvénynek, ami müveletet végez vele
print(result)               # és visszaadja a művelet eredményét amit eltárolok egy változóban
print(duplaz(7))            # vagy kiirathatom egyből



def nevjegy():              # a függvény törzsében levő össze utasítás végrehajtódik
    print('--------------')
    print('Lutz Gizi')
    print('SZOFT_I_1_E')
    print('--------------')

nevjegy()