## Chapter 5, Exercise 4: Rivers ☑
""
rivers={
      
        'amazon':'brzail',
        'Ravi':'Pakistan',
       ' yangtze':'china',
       'Ganges river': 'Bangladesh',
       'Volga River' : 'Europe' ,
}

for river, country in rivers.items():
    print(f"the{river.title()}flos through{country.title()}.")
    
    print("\nthe following countries are in clude in this data set:")
    for country in rivers.values():
        print(F"-{country.title()}")
        
    print("\nthe following rivers are in clude in this data set:")
    for river in rivers.keys():
            print(F"-{river.title()}")

