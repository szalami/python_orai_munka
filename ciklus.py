for i in range(0,5):            # egyesével lépked a range intervallumában
    print(i, "Csabi", end=" ")  # ha nincs end akkor sort tör


print()

for j in range(0,50,5):         # a harmadik szám: hányasával lépkedjen
    print(j, end=" ")

print()

for k in range(0,50):           # ugyanaz mint a fenti csak bonyolultan :)
    if k % 5 == 0:
        print (k, end=" ")