male = [
    "Erik",
    "Lars",
    "Karl",
    "Anders",
    "Johan"
    ]
female = [
    "Maria",
    "Anna",
    "Margareta",
    "Elisabeth",
    "Eva"
    ]

y = input("Vilket name ska plockas bort från listorna? \n>")

if y not in male:       #kolla om input av y inte finns i listan male då ska de plockas bort från female
    female.remove(y)
else:                   #annars plocka den bort från male
    male.remove(y)

print('Män:', male)         #skriv ut male listan
print('kvinnor:', female)   #skriv ut female listan