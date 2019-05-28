number = input("Multiplication table of the number: ")
countstart = 1
countend = 4
product = 0

while True:
    for x in range(countstart, countend):   # multiplicera talet med tal från countstart till countend
        product = int(number) * x
        print(product)
    
    question = input("Want to continue?: ")

    if question.title() == "Yes":
        countstart += 3 # lägg till 3 i countstart och countend för att gå från t.ex. 1-3 till 4-6
        countend += 3
        continue        # loopa while loopen igen
    elif question.title() == "No":
        break           # breaka ur loopen och stäng av programmet