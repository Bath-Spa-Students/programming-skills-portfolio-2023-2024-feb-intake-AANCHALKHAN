def describe_city(city, country='pakistan'):
    "Describe a city."
    msg=(f"{city.title()} is in {country.title()}.")
    print(msg)
    
describe_city('Sydney' ,'Australia')
describe_city('London', 'United Kingdom')
describe_city('Reykjavik','Iceland')
describe_city('Lahore',)
describe_city('Karachi')