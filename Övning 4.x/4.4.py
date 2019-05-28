förnamn = ["Maria", "Erik", "Karl"]
efternamn = ["Svensson", "Karlsson", "Andersson"]

for nameComb1 in efternamn:     #ta alla namn i efternamn och kombinera den med alla förnamn
    for nameComb2 in förnamn:
        print(nameComb2 + " " + nameComb1)      #skriv ut alla kombinationer