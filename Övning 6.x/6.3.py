import os
import requests

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
req = requests.get(url)
res = req.json()

os.system('cls')
print("Artits: \nAriana Grande\nAvicii\nBlink-182\nBrad Paisley\nEd Sheeran\nImagine Dragon\nMaroon 5\nScorpions")
artistIn = input("Artist name: ")

for x in res["artists"]:
    if artistIn.title() == x["name"]:
        ID = x["id"]

urlNew = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + ID
reqNew = requests.get(urlNew)
resNew = reqNew.json()

os.system('cls')
artistDes = resNew["artist"]

print("Genres: ")
[print(genre) for genre in artistDes["genres"]]
print("\nYears Active: ")
[print(years) for years in artistDes["years_active"]]
print("\nMembers: ")
[print(member) for member in artistDes["members"]]