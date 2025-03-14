print("This is my name")
print('     ^^.__')
print('o----')
print(' ||||') #This is a string
print('*' * 10)
## The code is reading in cascade style
#####Variables

prices = 10 ##This is an integer
rating = 4.9 ##This is a float
name = 'John' ##This is a string
is_published = False ##This is a boolean
## where we have a box 
print(prices)

##Exercise 
##we check in a patient named John Smith. He's 20 years old and is a new patient.

namesPatient = 'John Smith'
agePatient = 20
isNewPatient = True 
###getting input

input('What is your name?')
##This is also like control tv you have to do differents operations
# we are going to put it in a variable
name = input('What is your name?')

##print option
print('Hi ' + name + 'my name is andres ')
personsName = input('What is your persons name? ')
colorsPerson = input('What is your favorite color? ')
print(f'My is david, and I know your name is {personsName} and your favorite color is {colorsPerson}')

##Basics Maths

##int() function
##float() function
##str() function

birth_year = int(input(f'I would like to make some maths so, tell me your birthdays day and I will tell you your age '))
agePerson = 2025 - birth_year
print(f'Your age is {agePerson}')
print(type(agePerson))

##Exercise#2
weightCustomer = float(input('What is your weight in pounds? '))
weightCustomerKilos = weightCustomer * 0.45
print(f'Your weight in Kilos is {weightCustomerKilos}')


### Diferents strings
course = "Python's for beginners"
courseOne = '''
Python's for "beginners"
Python is a democracy for everyone who wants to learn


'''

##Indexing
print(f'{course[0]}')

##Indexing reverse
print(f'{course[-2]}')
print(course[-1:-8])

##Indexing reverse
course = "Python's for beginners"
##This is a copy of the variable but no use the same memory 
another = course[:]
###Exercise 
name = "Jennifer"
print(name[1:-1])

##Formatted Strings 
##When you want dinaumically change the value of a string

first = 'Andres'
last = 'David'

message = first + last

##Complicated way
#message = first + ' [' + last + '] is a coder'
##Easy way
message = f'{first} [{last}] is a coder'
print(message)

##Srtngs method
course = "Python for beginners"
print(len(course))

##Srtngs method
course = "Python for beginners"
print(len(course))

print(course.upper())
print(course.lower())
##To access to this methdos we use dot notation 
##When a function is part of an obeject we call it a method 
## but when a function is independent from an object we call it a function
##Let and print does not belong to any objecto so we call it a funncution 

course = "Python for beginners"
##This finds the index
print(course.find('b'))
##REPLACE METHOD

course = "Python for beginners"
print(course.replace('beginners', 'Absolute beginners'))
print(course.replace('f', "F"))

### Boolean expresion 
## Do we have this?
print('Python' in course)
print(course.title())


#course.upper()
#course.lower()
#course.find()
#print(course.title()) It capitalizes the first letter of each word in the string.
#It converts the rest of the characters to lowercase.
#Words are considered as substrings separated by whitespace or non-alphabetic characters.
#course.replace()
#Math Operations 

#addition operation
print(10+3)
#substraction operation
print(10-3)
#multiplication operation
print(10*3)
#division operation
print(10//3)
#modilus operation
#this remians the division
print(10%3)
#exponent operation
print(10**3)


## AUGMENTED ASSIGNMENT OPERATORS
X = 10
X = X + 3
X += 3
print(x)

## substraction assignment operartor
x -= 3

##Operator Precedence
# 1. Parentheses
# 2. Exponentiation  
# 3. Multiplication 
# 4. Division
# 5. Addition 
# 6. Substraction

x = 10 + 3 * 2
print(x)

x = 10 + 3 * 2 ** 2
print(x)

#MATH FUNCTIONS

x = 2.9 
print(round(x))
# this functions always return a positive number and this function 
# always rounds up to the nearest number

print(abs(-2.9))
# this function always returns a positive number
# abs function return the absolute value of the number

# if you want to program that involves complex mathemathics calculationn 
#you need to import the MATH MODULE, a module in python is a separate file with some reusable code
# to import a module you use the import keyword
# to use a function from a module you use the dot notation
# import math.

import math 
print(math.ceil(2.9))
#minute 59:44

##CONDTIONAL STATEMENTS

is_hot = False
is_cold = True
if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
elif is_cold: 
    print("It it's a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

##Exercise 
## datos de entrada = house 1Million 
## credit good or not good
## house - 10%
## if not house - 20 % 
## Datos de salida = down payment

housePrice = 1000000
downPayment = 0
creditBuyer = bool(input(f'The credit for this buyer is good? '))
if creditBuyer == True:
    downPayment = housePrice * 0.10
else:
    downPayment = housePrice  * 0.20
print(f'The down payment for this buyer is ${downPayment}')

##if applicant has high income and good credit 
## Eligable for loan

##OR LOGICAL OPERATOR
has_high_income = True
has_good_credit = True 
has_criminal_record = False
if has_high_income and has_good_credit:
    print("Eligable for loan")
else:
    print("Not eligable for loan")

##OR LOGICAL OPERATOR

if has_good_credit or has_high_income:
    print("Eligable for loan, because at least one of the condition is true")

##NOT OPERATOR
# if the applicant has good credit and not has criminal record

if has_good_credit and not has_criminal_record:
    print("Elegible for loan, cause it isn't a criminal")
else:
    print("Not elegible for loan, because it is a criminal")