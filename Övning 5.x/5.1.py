Sex = input("Kön: ")
HairC = input("Hårfärg: ")
EyeC = input("Ögonfärg: ")

SexAr = ["man", "kvinna"]
HairAr = ["svart", "brun", "röd", "blond"]
EyeAr = ["brun", "blå", "grön"]
Char = ["DanielR", "RupertG", "EmmaW", "SelenaG", "MaspianT", "BaharS", "TobiasB", "JagexJ", "JoelB"]

Char[0] = [SexAr[0], HairAr[1], EyeAr[0], "Daniel Redcliff"]
Char[1] = [SexAr[0], HairAr[2], EyeAr[1], "Rupert Grint"]
Char[2] = [SexAr[1], HairAr[1], EyeAr[0], "Emma Watson"]
Char[3] = [SexAr[1], HairAr[1], EyeAr[0], "Selena Gomez"]
Char[4] = [SexAr[1], HairAr[0], EyeAr[0], "Maspian Totzie"]
Char[5] = [SexAr[1], HairAr[1], EyeAr[0], "Bahar Sarah"]
Char[6] = [SexAr[0], HairAr[1], EyeAr[0], "Tobias Bo0beK"]
Char[7] = [SexAr[0], HairAr[0], EyeAr[0], "Jagex JJ"]
Char[8] = [SexAr[0], HairAr[3], EyeAr[1], "Joel Blue"]

for x in Char:
    if(Sex == x[0] and HairC == x[1] and EyeC == x[2]):
        print("Du liknar: " + x[3])