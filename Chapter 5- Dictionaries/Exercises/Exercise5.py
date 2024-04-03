## Chapter 5, Exercise 5: Pets ☑
#make an empty list t store the pets in.
pets={}

pet1={"Animal type": "Rabbit", "Onwer": "marry", "Pet name": "dodo", }
pet2={"Animal type": "cow", "Onwer": "Aanchal",  "Pet name": "moow"}
pet3={"Animal type": "wolf", "Onwer": "sam", "Pet name": "lulu"}
pet4={"Animal type": "cat", "Onwer": "cyrus" ,"Pet name": "kitty"}

pets=[ pet1,pet2,pet3,pet4]
for pet in pets:
    print(f"\nAnimal type: {pet['Animal type']}")
    print(f"Onwer: {pet ['Onwer']}")
    print (f"Pet name: {pet ['Pet name']}")