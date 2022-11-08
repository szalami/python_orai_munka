fp = open("adat.txt", "w", encoding="UTF-8")        # egy fájlt olvasok vele
                                                    # write w - írásra, ha nincs ilyen fájl akkor létrehozza, ha már van akkor felülírja
                                                    
                                                    # read r - olvasásra
                                                    # append a -hozzáfüzésre

fp.write("alma" + "\n")            # írok a fájlba                    
fp.write("körte" + "\n")           # írok a fájlba

fp.close                    # ha kész le kell zárni