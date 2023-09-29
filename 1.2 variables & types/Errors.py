print("Error snippets")
# some common errors people often make

Syntax error
# Bad
my variable = input("WHO GOES THERE? ")
print(my variable)
# Good 
my_variable = input("WHO GOES THERE?")
print(my_variable)

Name error
# Bad 
myGrandma = input("How's your Grandma doing? 😘 ")
print(mygrandma) # mygrandma wasn't defined
# Good
myGrandma = input("How-s your Grandma doing?")
print(myGrandma)
