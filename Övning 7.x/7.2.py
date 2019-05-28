from random import randint

triesLim = 1    # antal försök

print("I AM THE RNG ROBOT, CAN YOU GUESS MY NUMBER? \n")

maxVal = input("MAXIMUM VALUE: ")   # välj sitt eget range av nummer som ska genereras
number = randint(0, int(maxVal))    # slumpa fram ett tal från 0 till maximum talet

while 0 < triesLim: # när antal försök är mer än noll ska loopen köras (vilket kommer alltid att gälla tills loopen breakas)
    guess = input("\nYOUR GUESS: ") # gissning
    if int(guess) > number: # om gissningen är högre än talet ska den säga att gå mindre
        print("LOWER!")
        triesLim += 1   # räkna upp antal försök
    elif int(guess) < number:   # om gissningen är mindre än talet ska den säga att gå högre
        print("HIGHER!")
        triesLim += 1   # räkna upp antal försök
    else:
        print("INDEED, THE NUMBER " + guess + " IS CORRECT. \nIT TOOK YOU " + str(triesLim - 1) + " TOO MANY GUESSES.")
        break   # när gissningen är rätt, breaka ur loopen