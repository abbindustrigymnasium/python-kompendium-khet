import os
import requests

def get(url):
    req = requests.get(url)
    res = req.json()
    print(res)

def line(arg = False):
    if arg == False:
        print("------------------------------")
    else:
        print("******************************")

def header(arg):
    space = ""
    length = ((28 - len(arg)) / 2) - 1 
    while length >= 0: 
        space += " "
        length -= 1 
        title = "|" + space + arg + space + "|"
    print(title)

def echo(arg):
    print("| " + arg)

def prompt(arg):
    str(input("| " + arg + " >"))

def clear():
    os.system('cls')