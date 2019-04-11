Nord = ["Denmark", "Finland", "Iceland", "Norway", "Sweden"]
UK = ["England", "Ireland", "Scotland", "Wales"]
Country = input("Your Country: ")

if(Country.title() == Nord):
    print(Country.title() + " is in the Nord")
elif(Country.title() == UK):
    print(Country.title() + " is in the UK")
else:
    print(Country.title() + " is not in either the UK or the Nord")