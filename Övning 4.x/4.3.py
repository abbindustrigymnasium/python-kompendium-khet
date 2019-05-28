registrerade =["Anna", "Eva", "Erik", "Lars", "Karl"]
avanmälningar =["Anna", "Erik", "Karl"]

for person in avanmälningar:        #tabort alla namn i avanmälningar från registrerade
    registrerade.remove(person)

print(registrerade)     #skriv ut de registrerade