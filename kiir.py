fp = open("adat.txt", "w", encoding="UTF-8")        # egy fájlt olvasok vele
                                                    # write w - írásra
                                                    # read r - olvasásra
                                                    # append a -hozzáfüzésre

fp.write("alma")            # írok a fájlba                    
fp.write("körte")           # írok a fájlba

fp.close                    # ha kész le kell zárni