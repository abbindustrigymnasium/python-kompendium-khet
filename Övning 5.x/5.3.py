Nord = ["Denmark", "Finland", "Iceland", "Norway", "Sweden"]
UK = ["England", "Ireland", "Scotland", "Wales"]
Country = input("Your Country: ")

if(Country.title() == Nord):    #kolla om landet i input finns i Nord listan
    print(Country.title() + " is in the Nord")
elif(Country.title() == UK):    #kolla om landet i input finns i UK listan
    print(Country.title() + " is in the UK")
else:                           #kolla om landet i input finns varken i Nord eller UK listan
    print(Country.title() + " is not in either the UK or the Nord")