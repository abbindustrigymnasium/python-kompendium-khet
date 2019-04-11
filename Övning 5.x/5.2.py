NameIn = input("What's your name: ")
AgeIn = input("How old are you: ")

Age = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14" , "15", "16"]
Sleep = ["14", "13", "12", "11.5", "11", "11", "10.5", "10", "10", "10", "9.5", "9", "9", "9", "9", "8.5"]
SleepArrayCounter = int(AgeIn) - 1

for x in Age:
    if(AgeIn == x):
        print(NameIn.title() + ", you need to sleep at least " + Sleep[SleepArrayCounter] + " hours a day.")

if(int(AgeIn) > 16):
    print(NameIn.title() + ", you need to sleep at least 8 hours a day.")