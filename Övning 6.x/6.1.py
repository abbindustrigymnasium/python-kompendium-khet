import requests

Number = input("Your Number: ")
url = "http://77.238.56.27/examples/numinfo/?integer=" + Number
req = requests.get(url)
response = req.json()

print (response)

if(response['even'] == True):
    print("This number is and even number")
else:
    print("This number is an odd number")

if(response['prime'] == False):
    print("This number is not a prime number")
else:
    print("This number is a prime number")