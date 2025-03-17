##KEYWORDS ARGUMENTS
## The combination of having the parameter name followed 
# by it's value is what we call a keyword argument.

print("Start")
def greeting(first_name, last_name):
    print(f'Hello {first_name} {last_name}')
    print("Bye")

user_name = input("What is your name: ?")
user_last_name = input("What is your last_name: ?")

greeting(last_name=user_last_name, first_name=user_name)
print("Ends")

##Conclusion:
##C✅ If you use positional arguments, use them for all parameters (if it's simple).
##C✅ If you use keyword arguments, use them for all parameters (for clarity).
##C✅ If you mix them, positional must come first!