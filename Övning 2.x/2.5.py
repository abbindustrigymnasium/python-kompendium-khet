import os
import math

os.system('cls')
x1 = int(input("2 vanliga korvar: "))
x2 = int(input("3 vanliga korvar: "))
y1 = int(input("2 vanliga veganska korvar: "))
y2 = int(input("3 vanliga veganska korvar: "))

x3 = int(math.ceil((x1 * 2 + x2 * 3) / 8))
y3 = int(math.ceil((y1 * 2 + y2 * 3) / 4))

z1 = x1 + x2 + y1 + y2

os.system('cls')
print(str(x3) + " korv förpackningar\n" + str(y3) + " veganska korv förpackningar.")
print(str(z1) + " dryckor")

a1 = x3 * 20.95
a2 = y3 * 34.95
a3 = z1 * 13.95

b = a1 + a2 + a3

print("summan: " + str(b) + " SEK")