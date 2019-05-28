import requests     # hämta requests för att kunna dra saker från en dictionary

Number = input("Your Number: ")
url = "http://77.238.56.27/examples/numinfo/?integer=" + Number # api lnken med ett tal som ska checkas om det är jämn/udda, primtal eller inte
req = requests.get(url)
response = req.json()

print(response)

if(response['even'] == True):   # om talen är jämna eller udda
    print("This number is and even number")
else:
    print("This number is an odd number")

if(response['prime'] == False): # om talen är en primtal eller inte
    print("This number is not a prime number")
else:
    print("This number is a prime number")