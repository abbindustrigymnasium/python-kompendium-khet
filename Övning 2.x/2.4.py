print("Hur gammal är du?")
x = int(input("> "))

if (x < 18):    #om värdet är mindre än noll ska den visa om hur många år tills man blir myndig
    y = 18 - x
    print("Du är myndig om " + str(y) + " år!")
else:           #annars säger den att maan är redan myndig
    print("Du är redan myndig!")