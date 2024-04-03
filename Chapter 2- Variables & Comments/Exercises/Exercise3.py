# Exercise 3: Stripping Names
#Tidy up the code to make it easier to understand
#Use a variable to represent a person’s name, and include some
#whitespace characters at the beginning and end of the name.
#Make sure you use each character combination, “\t” and “\n”, at least once.



name = "\t Aanchal Nasrullah\n"

print("Unmodified:")
print(name)

print("\nusing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())