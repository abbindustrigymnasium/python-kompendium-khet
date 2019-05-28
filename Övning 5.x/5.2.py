NameIn = input("What's your name: ")
AgeIn = input("How old are you: ")

Age = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
Sleep = ["14", "13", "12", "11.5", "11", "11", "10.5", "10", "10", "10", "9.5", "9", "9", "9", "9", "8.5"]
SleepArrayCounter = int(AgeIn) - 1      #en counter för sleep listan beroende på AgeIn

for x in Age:
    if(AgeIn == x):     #kolla på AgeIn och om det är lika med x värdet i Age då ska det skriva ut antalet timmar med hjälp av SleepArrayCounter
        print(NameIn.title() + ", you need to sleep at least " + Sleep[SleepArrayCounter] + " hours a day.")

if(int(AgeIn) > 16):    #om man är äldre än 16 ska man sova minnst 8 timmar per dag
    print(NameIn.title() + ", you need to sleep at least 8 hours a day.")
elif(int(AgeIn) < 0):   #troll input skall blockeras ut
    print("You are not even born!11!!1")