import requests
import func

func.line(True)
func.header("ARTIST DATABASE")
func.line(True)
func.echo("L | List artists")
func.echo("V | View artist profile")
func.echo("E | Exit")
choice = func.prompt("")

yeet = True

while yeet: # kör när den yeetar (kör precis samma kod som 6.3)
    yes = func.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")
    if choice.title() == "L":
        func.clear()
        func.line(True)
        func.header("ARTIST DATABASE")
        func.line(True)

        for x in yes["artists"]:
            func.echo(x["name"])

        func.line()
        func.echo("L | List artists")
        func.echo("V | View artist profile")
        func.echo("E | Exit")
        choice = func.prompt("")
    elif choice.title() == "V":
        func.clear()
        func.line(True)
        func.header("ARTIST DATABASE")
        func.line(True)
        artistIn = func.prompt("Artist name")
        
        for x in yes["artists"]:
            if artistIn.title() == x["name"]:
                ID = x["id"]
        
        sey = func.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + ID)
        artistDes = sey["artist"]

        [func.echo("Genres: ") for genre in artistDes["genres"]]
        [func.echo("Years Active: ") for years in artistDes["years_active"]]
        [func.echo("Members: ") for member in artistDes["members"]]
    elif choice.title() == "I":
        yeet = False
    else:
        func.line(True)
        func.header("ARTIST DATABASE")
        func.line(True)
        func.echo("Selection invalid")
        func.line()
        func.echo("L | List artists")
        func.echo("V | View artist profile")
        func.echo("E | Exit")
        choice = func.prompt("")