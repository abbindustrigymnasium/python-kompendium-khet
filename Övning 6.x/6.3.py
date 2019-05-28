import os
import requests

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
req = requests.get(url)
res = req.json()

os.system('cls')
print("Artits: \nAriana Grande\nAvicii\nBlink-182\nBrad Paisley\nEd Sheeran\nImagine Dragon\nMaroon 5\nScorpions")
artistIn = input("Artist name: ")

for x in res["artists"]:        # hitta artisten som man har anropat i input
    if artistIn.title() == x["name"]:
        ID = x["id"]    # ta artistens ID

urlNew = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + ID        # lägg till IDn bakom länken för att få artisternas informationer
reqNew = requests.get(urlNew)
resNew = reqNew.json()

os.system('cls')
artistDes = resNew["artist"]

print("Genres: ")
[print(genre) for genre in artistDes["genres"]] # skriv ut artistens alla genre
print("\nYears Active: ")
[print(years) for years in artistDes["years_active"]]   # skriv ut artistens år tal som de var/är aktiva i
print("\nMembers: ")
[print(member) for member in artistDes["members"]]      # skriv ut alla av artistens medlemmar