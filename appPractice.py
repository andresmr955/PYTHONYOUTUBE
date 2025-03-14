## Comparison Operators
## ==, !=, >, <, >=, <=

temperature = 30

if temperature > 30: 
    print("It's a really hot day")
elif temperature == 30:
    print("It's a hot day")
elif temperature < 30:
    print("It is a cold day")


## Exercise

name = input("I am going to tell you, how many characters has your name, so please tell me What's your name?")

if len(name) < 3: 
    print("Your name it should be at least 3 characters")
elif len(name) > 50: 
    print("Your name can be a maximum of 50 characters")
else:
    print(f'Your name is good, {name}, and the length of your name is {len(name)}')