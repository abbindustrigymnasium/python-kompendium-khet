req = input("1. KM to Miles\n2. Miles to KM\n> ")   # alternativ för att antingen konvertera km till mil eller tvärtom
number = input("Distance > ")   # anropa talet som ska konverteras

def KMtoMiles(distance):    # funktion för att konvertera km till mil
    x = float(number)
    print(x * 0.62137)

def MilestoKM(distance):    # funktion för att konvertera mil till km
    x = float(number)
    print(x * 1.60934)

if(req == "1"):     # om req är att konvertera km till mil, gör det
    KMtoMiles(number)
elif(req == "2"):   # om req är att konvertera mil till km, gör det
    MilestoKM(number)