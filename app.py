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

##CONDITIONAL STATEMENTS

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

    #WHILELOOPS

#While condition:
#    do something ...

#Example

i = 1
while i <= 5:
    print(i)
    i += 1
print("Well Done")


#Example repeat a string
j = 1
i = 1
while i <= 5:
    print('*' * i)
    i += 1
    
print("Well Done")
## For LOOPS

#String: is a secuence of character

for item in 'python':
    print(item)
# List is a list of items, objects, customer, emails
for item in ['Mosh', 'John', 'Sara']:
    print(item)
for item in [1,2,3,4,5,6]:
    print(item)
##RANGE FUNCTION

for item in range(10):
    print(item)

# range can start with a number and it can end with other but it doesn't show it
for item in range(5,10):
    print(item)
# the third value works to go steps forward
for item in range(5,10, 2):
    print(item)
##NESTED LOOPS
#CORDINATES IS A X AND Y 
for x in range(4):
    for y in range(3):
        print(f'{x}, {y}')
##LISTS
#A list a is type of data that we can store differents elements like numbers, booleans, and string 
names = ['John', 'bob', 'Mosh ', 'Sarah', 'Mary']
print(names[2])
print(names[-2])
print(names[2:]) #Rerturn all the items after 2 item
print(names[2:4])
print(names[2:4])

###2Dimension LISTS
##data science and maching learning

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
#using square brackets we can access individial items
matrix[0][1] = 20
print(matrix[0][1])
print(matrix)

##USING LOOP

matrixa = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrixa:
    for item in row:
        print("This is the matrix in a loop", item )

##LIST METHODS
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)
numbers.insert(0,10) ## with this method is necessary to add the index and the object or element where you want to insert it.
print(numbers)
numbers.remove(5)  ## it removes the item you want to delete
numbersstring = ["David","Andres",5, 2, 1, 7, 4]
print(numbersstring)
numbersstring.remove("David")  ## it removes the item you want to delete
print(numbersstring)
#numbers.clear() ## It deletes all items
print("This is the list ", numbers)
indexValue = numbers.index(7)
print(indexValue) ## it returns the index of the value that you put inside the brackets

print(5 in numbersstring)
print(50 in numbers)
numbersx = [5, 2, 1, 7, 4, 5]
print(numbersx.count(5)) ## it counts how many times is an item in a list
numbersx.sort()
print("sort method",numbersx ) ##This method puts the items in order or in a group
##NONE is an object in python that represents the absence of a value
numbersx.reverse()
print("Reverse method", numbersx) ##This method reverses the items of our list
numbersx.copy() ## This method has to be declared in a new variable and it is going to copy all element in it, but you can midify the new variable and it is not going affect the original

##WRITE A PROGRAM TO REMOVE THE DUPLCAITES IN A LIST 


lista = [2, 2, 4, 6, 3, 4, 6, 1]
duplicados_eliminados = []


for item in lista:
    cuantasVeces = lista.count(item) 
    if cuantasVeces > 1:
        duplicados_eliminados.append(item)
        lista.remove(item)
print(lista)
print(duplicados_eliminados)

##TUPLES 
## The tuples are similar but to list to store values, there are key difference between list and tuples
## The tuples are immutabily and we use paretheses and are faster than the lists

numbers = (1,2,3)
print(numbers[0])

##UNPACKING
##Unpacking in Python allows you to assign elements of a list or tuple to multiple variables in a single line.
coordinates = (1, 2, 3)
coordinates[0] * coordinates[1] *  coordinates[2] 

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x * y * z

x,y,z = coordinatesa

##Dictionaries 
## It is data structure that stores information as key-value pairs. with curly braces
## the keys should be unique

customer = {
    "name": "Andres Smith",
    "age": 26,
    "is_verified": True
}

print(customer["name"])


##METHOD
print("This is the brthday",customer.get("birthday"))
print("This is the name", customer.get("name"))

## if you want to see a  key-value, but it does not add it to the dictionary
print(customer.get("birthday", "17/03/25"))
print(customer)

##modifie a key-value
customer["name"] = "Jack Smith"
print(customer)
