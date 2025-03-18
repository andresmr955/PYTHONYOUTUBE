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


##EMOJI CONVERTER

message = input("Write user: ")
words = message.split(' ') ##This method help us to divide the string every time that finds a space 
print(words)


emojis_dictionary = {
    ":)" : "😀",
    ":(" : "😔"
}
output = ""
for word in words:
    output += emojis_dictionary.get(word, word) + " "
print(output)
##FUNCTIONS 

#Yes! Functions in Python are blocks of reusable code that you can call whenever needed. They help organize code, avoid repetition, and make programs easier to read and maintain.

def greet_user(): 
    print('''
    Hello there
    Welcome aboard
    ''')


print(greet_user())

## There is an order in python how it calls every element of the document
## you have to create the function first before to call it 

##PARAMETERS
## Yes, exactly! Parameters in a function are like placeholders or characteristics that the function expects when it's called. They allow you to pass data into the function to be used within its body.
## We are obligated to pass the parameter of the function

print("Start")
def greeting(name, last_name):
    print(f'Hello {name} {last_name}')
    print("Bye")

user_name = input("What is your name: ?")
user_last_name = input("What is your last_name: ?")

greeting(user_name, user_last_name)
print("Ends")


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

##RETURN STATEMENT
## This is so functional if you are doing calculation and you want to return an item

def square(number):
    return number * number

#result = square(3)
print(square(3))

## by default all functions return none

### CREATE A REUSABLE FUNCTION
input_user = input("Write anything: ")

def emojiConverter(customer_phrase):
    words = customer_phrase.split(' ')
    dictionary_emoji = {
        ":)" : "😃",
        ":(" : "😔",
        ":p" : "😋"
    }


    output_customer = ""
    for item in words:
        output_customer += dictionary_emoji.get(item, item) + " "
    return output_customer

print(emojiConverter(input_user))

##Exceptions 
## How to handle errors
## as a good python programmer you should anticipate any kind of error that the user can cause and handle properly
## you have to show to the customer how he can proceed after cause because he did not properly read

##example crash
#age = int(input('Age: '))
#print(age)

## good example not crash

try: 
    age = int(input('Age: '))
    income = 20000
    risk = income / age ## this can not be handle with the exception Value error because is a divion by 0
    print(age)
except ZeroDivisionError: 
    print("Age can not be zero")
except ValueError:
    print('Invalid Value')

##COMENTS 
## you have to avoid what the code does, of course and is obvious, can create noise
## just to explain why and house?
## too much of good thing is bad thing


##CLASSES
## We use to defined new types
## These classes can have methods that we define in the body of the class
## The classes can have attributes that we can set anywhere in out programs
## Numbers 
##Strings
##Booleans 
##----------------
##Lists 
##Dictionaries

##we capitalized the first letter of each word in classes
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

## An object is an instance of a class

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.__dict__)
print(dir(point1))

point1.draw()



point2 = Point()
point2.x = 1
print(point2.x)

import types
## CLASSES CREATED BY ME

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


    def running(self):
        carruns = "Car runs"
        return carruns
    
    
    def stopping(self):
        carstops = "Car stops"
        return carstops
carToyota = Car("Toyota", 180)
##to check the arguments
print(carToyota.__dict__)
print(carToyota.running())
print(carToyota.stopping())

## Adding an parameter after been created

carToyota.color = "Red"
print(carToyota.__dict__)

## Adding a function after been created with a module 

def honk(self):
    return f"{self.brand} is honking!"

carToyota.honk = types.MethodType(honk, carToyota)
print(carToyota.honk(), " with a module")


## Adding a function after been created without a module DIRECTLY

carToyota.honk = honk.__get__(carToyota)
print(carToyota.honk(), " without a module")

## CONSTRUCTORS
## A constructor is a special method named __init__() that gets called with underscore
# at the time of creating an object

class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def move(self):
        print("move")
    def draw(self):
        print("draw")

point = Point(10,20)
point.x = 86
print(point.x)

## Define a new type called person
## name an attribute 
## talk() as a method

class Person():
    def __init__(self, name):
        self.name = name


    def talk(self):
        xreturn = "He talks"
        return xreturn
person_one = Person("Andres")
print(person_one.talk())
print(person_one.__dict__)

bob = Person("bob")
print(bob.talk())
print(bob.__dict__)
##Inheritance
##In programming we should not define something twice
## We define a new class called Mammal and we move the methdo right there
## The idea of taking one class and extending it to make something new
## We can reuse an existing class and inherit all the capabilities of an existing class and then add our our own little bit to make our new class

class Mammal: 
    def walk(self):
        print("walk mammal")

class DogMa(Mammal):
    def bark(self):
        print("break")
    def be_annoying(self):
        print("annoying")        

## Python does not like an empty classes, so it is better to put pass
class CatMa(Mammal):
    pass

##This is bad, because is not DRY 
class Dog:
    def walk(self):
        print("walk")
##This is bad also, because is not DRY 

class Cat:
    def be_annoying(self):
        print("annoying")        

dog1 = Dog()
dog1.walk()

dog2m = DogMa()
dog2m.walk()

cat1 = CatMa()
cat1.walk()

cat2 = Cat()
cat2.be_annoying()

print("FREECODECAMP CLASS")
###FREECODECAMP YOUTUBE

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, name):
        self.name = name
        print(self.name, "constructed")
    def party(self) :
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7 
        self.party()
        print(self.name, "points", self.points)

### create the objects according to the class        

s = PartyAnimal("Saly")
s.party()
print(s.__dict__)

j = FootballFan("Jim")
j.party()
j.touchdown()
print(j.__dict__)

##Conclusions
## Class is a template or shape
## Attribute - a variable within a class
## Method -  a function within a class
## Object - A particualr instance of a class
## Inheritance - The ability to extend a class to make a new class


##Modules
## It is a file with some python code
# We use modules organize our code, just like section in supermarket
# we have ability to reuse our code
##Instead of writing all the code, instead of writing all the functions in one file, you break up 
# our code across multiple file. Each file is called Module
# It should contain all the related functions and classes

##IMPORT THE ENTIRE MODULE
import converters
##print it out
print("This is from kg to lbs=> ", converters.kg_to_lbs(70))

## The second option, to use the specifics functions from that module
from converters import lbs_to_kg

lbs_to_kg(100)
##print it out
print("This is from lbs to kg=> ", lbs_to_kg(100))
##PACKAGES 
## Package is a container for multiple modules, in file system terms a package is  a directory or folder.
## We can have modiles for sales, shipping, customer service
##__init__.py when Python interpreter sees a file with this name and name in a directory, it threats this directory as a package  
##GENERATING RANDOM VALUES
##Python comes with a standrd library that contains several modules 
# that contains several modules for commontask such as sending email, .
# working with date and time, generating random values and passwords and so on 
# There are several modules already built into Python and that means there is already lots of functionality
#  taht we can reuse
# 

##RANDOM MODULE
import random 

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))


members = ['John', 'Mary', 'bob', 'Mosh']
leader = random.choice(members)

print(leader)

##FILES AND DIRECTORIES
## https://docs.python.org/3/py-modindex.html
## pathlib: Classes that we can use to create objects to work with directories 
import shutil
from pathlib import Path 


##Creating dir
#path = Path("ecommerceexample")

##checking if exists the path
#print(path.exists())
##Creating directory
#print(path.mkdir())
##Deleting dir
###if path.exists() and path.is_dir():
###    try:
###        path.rmdir()
###        print("Directory removed successfully")
###    except PermissionError:
###        print("Permission denied: Unable to remove directory")
###    except Exception as e:
###       print(f"Error: {e}")
###        else:
###            print("Directory does not exist or is not a directory")
##Absolute path: For absolute path we start of our hard disk
##Relative path
##If you wanna to reference this ecommerce directory in our project
#can use the relative path

## We can search for a files or directories that we need to pass a
# a current path
#print(path.glob())

#* means all filles and all directories
#print(path.glob('*'))
#You optionally add an extension .*, the current files but not the directories
#print(path.glob('*.*'))
#You can also search all py files
#print(path.glob('*.py'))
#You can also search all xls 
#print(path.glob('*.xls'))


##This reads all py files
#path = Path()

#for file in path.glob('*.py'):
#    print(file)


##This reads all  files
path = Path()

for file in path.glob('*'):
    print(file)

    ##Pypi and pip
#Pypi is an open source web where we found differents pacakages that we use for differents tasks

'''
Multiline comments: they are written using triple double quotes (“”” or ‘’') to open the comment and to close it. Everything between these two marks will be ignored by the Python interpreter.
“"”
This is a multi-line
multi-line comment
“"”'
''
'''