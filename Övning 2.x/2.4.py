print("Hur gammal är du?")
x = int(input("> "))
if (x < 18):
    y = 18 - x
    print("Du är myndig om " + str(y) + " år!")
else:
    print("Du är redan myndig!")