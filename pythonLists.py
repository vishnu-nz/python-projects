# Easy Example

# List are fundamental data structure in Python, used to store collections of items. They can hold various types of data, including numbers, strings, or even other lists

# Creating a list
fruits = ["apple","banana","cherry"]

# accessing elements
print(fruits[0])

#Modifying elements
fruits[1] = 'grape'
print(fruits)

# Adding elements
fruits.append('orange')
print(fruits)

# Removing elements
fruits.pop()
fruits.remove()

# Medium Example

# Write a program that finds the sum of all elements in a list of numbers.

# List of numbers
numbers = [1,2,3,4,5]

#Initialize a variable to store the sum
sum_of_numbers = 0

#calculate the sum

for num in numbers:
    sum_of_numbers += num

print("Sum of the numbers:-",sum_of_numbers)

# Hard Program

# Write a program that finds the common elements between two lists

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

common_elements = []

for item in list1:
    if item in list2:
        common_elements.append(item)

print("Common Elements:- ",common_elements)