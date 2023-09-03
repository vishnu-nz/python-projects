# Variables and Data Types
# Best Practices
# 1. Varibale names does not start with numbers
# 2. Variable names always start with lower case
# example --> 
name = 'Vishnu'
# To know the type of the string use type() function
type(name)
type(2j) # complex type example

a = 5  # Assign Operator
5 == 5 # Comparision operator

# the basic data types so far learned

# Numbers, Strings, Booleans

## Data Structures

#List 
my_list = [1,2,3]
print(my_list)
len(my_list)

# you can have list of list
my_list = [[1,2,3],[False,True],[]]

# SETS

my_set = {1,2,3,4}
type(my_set)
len(my_set)
# sets returns a unique elements

# TUPLES
# my_tuples =(1,2,3)
# you can not modify elements in Tuples
# tuple object has no attribute append
# once a tuple is declared, you can not add to it or change any of the values in it#
# why use Tuples
# They are memory efficient
# Good for sorting lots of little things like x,y coordinates

#DICTIONARIES
my_dict = {
    'apple': 'A red fruit',
    'bear' : 'A scary animal'
}

# SETS & DICTIONARIES

# both are defined with curly brackets
# Sets have unique values, dictionaries have unique keys
# The order does nott matter


# OPERATORS

# Arithmetic Operators

1+1
4*5
5 ** 2 # Exponent
20 / 4 # Division in return will get float values only
20 % 6 # Modulos Operator will get the remainder

'string 1 ' + 'String 2 ' # + Concatinates the two strings
'-- String1 --'* 4 # Repeats the string 4 times

# Comparision Operators

4 == 5
4 > 5
4 <= 5

# Logical Operators # and, or, not

# Membership Operators --> in  ---> not in
1 in [1,2,4] # retruns the True (Boolean)
10 not in [1,5,4,55] # returns False

# Control Flow

# if/else

a = True
b = True
c = True

if a:
    print("It is True")
    print("Also print this")
    if b:
        print('Both are true')
        if c:
            print('All three are True')
else:
    print('It is false')
print('always print this')

# For Loops
a = [1,2,3,4,5]

for item in a:  # in is in for loop syntax
    print(item)

# While loops

a = 0
while a < 5:
    print(a)
    a = a + 1

# Functions

print('hello World') # print is a function

# we can make our own functions with a key word called def

def multiplyByThree(val):
    return 3 * val

# Now use our function ike below
multiplyByThree(4)


def multiply(val1,val2):
    return val1 * val2

# call our function we defined multiply like below
multiply(3,4)

a = [1,2,3] # assigning a list
def appendFour(myList):
    myList.append(4)

# call our function we defined appendFour
appendFour(a)
print(a) # To see the output

# print funtion returns None -- None Type

### CLASSES & OBJECTS

# you have to define a class with name

class Dog: # Class name is Dog -- best practice is to keep class names always start with Capital letters and variables and functions with lowercase
    def __init__(self, name): # Class Definitions -- init function  is initilization
        self.name = name # These are the attributes of the objects
        self.legs = 4 # These are the attributes of the objects

    def speak(self): # These are the class methods here the class method is speak
        print(self.name + ' Says: Bark!')

# Now calling our class like below

my_dog = Dog('Rover')  # my_dog is a newly created instance of class Dog

another_dog = Dog('Fluffy') # another_dog is a newly created instance of class Dog

my_dog.speak()
another_dog.speak()

type(Dog('Rover'))

# casting
int(8.99) # built in class in Python line str list float all are classes. Here we are casting from float to int




