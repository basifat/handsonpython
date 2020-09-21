#Saturday 22/08/2020

# Functional programming pipeline

# Function Generators

# Funtion typings

# Aliasing functions

# Arbitrary keyword arguments for a function

# Unpacking

#Example
list_numbers =[1,2,3,4,5,6,7,8,9,10]

def transform(numbers):
    result = []
    for number in numbers:
        result.append(number * 5)
    return result

num =transform(list_numbers)
print(num)
#output is 
#[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# can also be simplified as below
transform_numbers = [number * 5 for number in list_numbers]
print(transform_numbers)
#output is
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

def multiply(number):
    return number * 5

def transform(numbers):
    result =[]
    for number in numbers:
        result.append(multiply(number))
    return result

num =transform(list_numbers)
print(num)

transform_numbers =[multiply(number) for number in list_numbers]
print(transform_numbers)
#output is
#[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


#list comprehension
#we want to add 1 to any number greater than 25 otherwise subtract 1
#we need to do the expression before the checks
#we can't do assignment statement in list comprehesion
transform_numbers_2= [number + 1 if number > 25 else number -1 for number in transform_numbers]
print(transform_numbers_2)
#output is 
#[4, 9, 14, 19, 24, 31, 36, 41, 46, 51]

# filtering : didn't work cos it still gave the same size
filtered_numbers = [number -1 if number > 25 else 0 for number in transform_numbers_2]
print(filtered_numbers)
#output is
# [0, 0, 0, 0, 0, 30, 35, 40, 45, 50]

# if we try else "None"
filtered_numbers = [number -1 if number > 25 else None for number in transform_numbers_2]
print(filtered_numbers)
#output is
# [[None, None, None, None, None, 30, 35, 40, 45, 50]


def multiply(number):
    return number * 5

def transform(numbers):
    result =[]
    for number in numbers:
        result.append(multiply(number))
    return result

num =transform(list_numbers)
print(num)
def filter_num(item):       
    # if item < 25:
    #     pass
    # else:
    #     return item
    return item > 25 # printed a boolean for us

transform_numbers =[multiply(number) for number in list_numbers]
transform_numbers_2= [number + 1 if number > 25 else number -1 for number in transform_numbers]
filtered_numbers = [filter_num(number) for number in transform_numbers_2]
print(filtered_numbers)
#output is
# [False, False, False, False, False, True, True, True, True, True]


# using builtin and checking if it satisfies our condition then we return the item
#we are interested in the number
def multiply(number):
    return number * 5

def transform(numbers):
    result =[]
    for number in numbers:
        result.append(multiply(number))
    return result

num =transform(list_numbers)
print(num)
def filter_num(item):       
    if item < 25:
        pass
    else:
        return item 

transform_numbers =[multiply(number) for number in list_numbers]
transform_numbers_2= [number + 1 if number > 25 else number -1 for number in transform_numbers]
filtered_numbers = [filter_num(number) for number in transform_numbers_2]
filtered_numbers_2 = list(filter(filter_num, transform_numbers_2))
print(filtered_numbers_2)
#output is 
#[31, 36, 41, 46, 51]


#using built in with predicate function. if we don't return item
def multiply(number):
    return number * 5

def transform(numbers):
    result =[]
    for number in numbers:
        result.append(multiply(number))
    return result

num =transform(list_numbers)
print(num)
def filter_num(item):       
    # if item < 25:
    #     pass
    # else:
    #     return item
    return item > 25 

transform_numbers =[multiply(number) for number in list_numbers]
transform_numbers_2= [number + 1 if number > 25 else number -1 for number in transform_numbers]
filtered_numbers = [filter_num(number) for number in transform_numbers_2]
filtered_numbers_2 = list(filter(filter_num, transform_numbers_2))
print(filtered_numbers_2)
#output is 
#[31, 36, 41, 46, 51]


#generator function***********************
def add(a):
    return a + 10

def gen_function(item):
    print("the first time")
    yield item
    
    print("the second time")
    yield item + 1
    
    print("the third time")
    yield item + 10
    
    print("the fourth time")
    yield item + 20
    
plus = add(10)
print(plus)
#output is 20

#calling the gen function
gen_result = gen_function(1)
print(gen_result)
#output is 
#<generator object gen_function at 0x7fd813b27f90>

#to get the figures out, we can use the 'next'function
print(next(gen_result))
#output is
#the first time
#1
print(next(gen_result))
#output is
#the second time
#2
print(next(gen_result))
#output is
#the third time
#11
print(next(gen_result))
#output is
#the fourth time
#21


##Another Example
numbers = [1,2,3,4,5,6,7,8,9] # assume it's 10 million transations 
def find_number(numbers):
    for number in numbers:
        print(number)

def gen_find_number(numbers):
    for number in numbers:
        yield number

find_number(numbers)
gen_num = gen_find_number(numbers)
print(gen_num)
#generator functions allow us take a single item out of an iterable without destroying the iterable
#we can't slice it like an array
print(next(gen_num))# output is 1
print(next(gen_num))# output is 2

for item in gen_num:
    result = item + 5
    print(result)
#output is 
# 1 - is for the next(gen_num)
#2 - is for the 2nd next(gen_num)
#8
#9
#10
#11
#12
#13
#14

#comment out the print statement above before runnung this
for item in range(1,5):
    result = next(gen_num)
    print(result)
#output is 
# 1
#2
#3
#4

#Timer delay in python***********************
import time
for item in range(4,5): #or use 'while True:
#when u exhaust a generator, it will raise a stop iteration
    time.sleep(5)
    result = next(gen_num)
    print(result)

#to run a timer and terminate it
def gen_timer():

    while True:
        time.sleep(1)
        try:
            result = next(gen_num) # [100000]
            print(result)
        except StopIteration:
            print("generator is exhausted")
            return 
gen_timer()

#Function Type hint*****************************************
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float

sub = f(22)
print(sub)
#output is 25.5

#Aliasing Functions
from functions_day_5_helper import g_add as sum_total # we rimport and rename incase the name already exist

# Arbitrary keyword arguments for a function*************************
# Write a function that have one parameter that collects as many arguments as possible
#Call the fucntion three time with different arguments

dico = {"a": 10, "b": 20}
print(dico)
#output is {'a': 10, 'b': 20}
#which is same as below
def manufacture_phones(**kwargs):
    return kwargs
result = manufacture_phones(iphone = 'xmax',samsung = 'g9')
print(result)
#output is {'iphone': 'xmax', 'samsung': 'g9'}

#** - means it can take multiple arguments
result = manufacture_phones(iphone = 'xmax',samsung = 'g9', motorola = 'b5')
print(result)
#output is {'iphone': 'xmax', 'samsung': 'g9', 'motorola': 'b5'}


#giving any number of postional argument
def manufacture_phones(*args,**kwargs):
    return (args, kwargs)

result = manufacture_phones(10,iphone = 'xmax',samsung = 'g9')
print(result)
#output is ((10,), {'iphone': 'xmax', 'samsung': 'g9'})


#explanation
# the version is the positional argument while the others are keyword argument
def manufacture_zero(version, iphone = None, samsung = None, motorola = None):
    return version, iphone, samsung, motorola

result = manufacture_phones(iphone = 'xmax',samsung = 'g9', motorola = 'b5', lg="lgx9")
print(result)

#Done*****************

