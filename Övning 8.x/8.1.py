req = input("1. KM to Miles\n2. Miles to KM\n> ")
number = input("Distance > ")

def KMtoMiles(distance):
    x = float(number)
    print(x * 0.62137)

def MilestoKM(distance):
    x = float(number)
    print(x * 1.60934)

if(req == "1"):
    KMtoMiles(number)
elif(req == "2"):
    MilestoKM(number)