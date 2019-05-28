import math     #importera matte definitionerna från math

x1 = int(input("2 vanliga korvar: "))
x2 = int(input("3 vanliga korvar: "))
y1 = int(input("2 veganska korvar: "))
y2 = int(input("3 veganska korvar: "))

x3 = int(math.ceil((x1 * 2 + x2 * 3) / 8))      #räkna ut hur många x korv förpackningar som ska köpas in
y3 = int(math.ceil((y1 * 2 + y2 * 3) / 4))      #räkna ut hur många y korv förpackningar som ska köpas in

z1 = x1 + x2 + y1 + y2                          #antal drycka per elev

print(str(x3) + " korv förpackningar\n" + str(y3) + " veganska korv förpackningar.")    #skriv ut antal korv förpackningar
print(str(z1) + " dryckor")                                                             #skriv ut antal dryckor

a1 = x3 * 20.95     #räkna ut priset för x förpackningar
a2 = y3 * 34.95     #räkna ut priset för y förpackningar
a3 = z1 * 13.95     #räkna ut priset för dryckor

b = a1 + a2 + a3    #totala kostnaden

print("summan: " + str(b) + " SEK")     #skriv ut den totala kostnaden dva x + y + dryckor