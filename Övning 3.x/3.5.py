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

if y not in male:
    female.remove(y)
else:
    male.remove(y)

print('Män:', male)
print('kvinnor:', female)
