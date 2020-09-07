# Example: To get unique item from a list
#Expected output: [1,2,3,4,5]
#define a function
#Initialise an empty list lst = []
#Read each number using a for loop
#In the for loop append each number to the list
#call the item and give it a variable
#print the variable
items = [1,1,1,2,2,2,3,4,5,5]
def unique_items():
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item) #Now we use predefined function 
    return unique
a = unique_items()
print(a) #Print the result


#modified so that any argument can go through it
#output is same as above
def unique_items(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique
duplicate= [1,1,1,2,2,2,3,4,5,5]
a = unique_items(duplicate)
print(a)

## To use python builtin 'set' to eliminate duplicates
duplicate= [1,1,1,2,2,2,3,4,5,5]
b = set(duplicate)
print(b)

## to change the 'set' to a list
duplicate= [1,1,1,2,2,2,3,4,5,5]
b = list(set(duplicate))
print(b)


#Example 2: Write a function that returns a list of items with every item now multiplied by 2
#output:[2,4,6,8,10]
# is a continuation of the code above
#define a function
#Initialise an empty list lst = []
#Read each number using a for loop
#In the for loop append each number to the list
#call the item and give it a variable
#print the variable
def multiply_by_two(items):
    c = []
    for item in items:
        item = item * 2
        c.append(item)
    return c

a = unique_items(duplicate)
multiplied = multiply_by_two(a)
print(multiplied)

#Map : this is using the builtin fuction to get the same result as above
#map retain same size of the original array
#i had to introduce 'list' because Python 3 'map' returns an iterator and 
# listing the elements of an iterator "consumes" it and there's no way to "reset" it
def multiply_item_by_two(item):
    return item * 2
mapped_two = list(map(multiply_item_by_two, a))
print(mapped_two)

#to map * 10
def multiply_item_by_ten(item):
    return item * 10
mapped_ten= list(map(multiply_item_by_ten, a))
print(mapped_ten)

#Higher order function that accept a function and a list***********
def our_map(fn, item_list):
    new_list = []
    for item in item_list:
        mapped = fn(item)
        new_list.append(mapped)
    return new_list

our_map_result = our_map(multiply_item_by_ten, a)
print(our_map_result)

#doing some optimisation, moving the function multiply_item_by_two(item) to the top
def multiply_item_by_two(item):
    return item * 2

def multiply_by_two(items):
    c = []
    for item in items:
        #item = item * 2 (this can be changed to below)
        item = multiply_item_by_two(item)
        c.append(item)
    return c

a = unique_items(duplicate)
multiplied = multiply_by_two(a)
print(multiplied)

#Example 3: Write a function that returns a list of items with only items greater than 3
# expected output = [4,5,6]
#define a function
#Initialise an empty list lst = []
#Read each number using a for loop
#In the for loop append each number to the list
#call the function and give it a variable
# print the variable

numbers = [0,1,2,3,4,5,6]

def greater_than_three(numbers):
    new_number = []
    for number in numbers:
        if number > 3:
            new_number.append(number)
    return new_number

filtered = greater_than_three(numbers)
print(filtered)


#another way to run it
#output is same as above
def item_greater_than_three(item):
    if item > 3: #boolean
        return True

def greater_than_three(numbers):
    new_number = []
    for number in numbers:
        if item_greater_than_three(number):
            new_number.append(number)
    return new_number

filtered = greater_than_three(numbers)
print(filtered)


#Doing the same thing above with the builtin function 'filter'
filtered_2 = list(filter(item_greater_than_three, numbers))
print(filtered_2)

#optimising
#4 > 3 # True
#1 > 3 # False
def item_greater_than_three(item):
    return item > 3

def greater_than_three(numbers):
    new_number = []
    for number in numbers:
        if item_greater_than_three(number):
            new_number.append(number)
    return new_number

filtered = greater_than_three(numbers)
print(filtered) # output is same 