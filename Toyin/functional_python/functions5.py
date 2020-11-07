#Saturday 22/08/2020

# Functional programming pipeline

# Function Generators

# Funtion typings

# Aliasing functions

# Arbitrary keyword arguments for a function

# Unpacking


list_numbers =[1,2,3,4,5,6,7,8,9,10]
def transform(numbers):
    """function to multiply numbers by 5
    Expected input = [1,2,3,4,5,6,7,8,9,10]
    Expected output = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    """
    result = []
    for number in numbers:
        result.append(number * 5)
    return result

num =transform(list_numbers)


"""can be simplified as
    Expected input = [1,2,3,4,5,6,7,8,9,10]
    Expected output = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
"""
transform_numbers = [number * 5 for number in list_numbers]




list_numbers =[1,2,3,4,5,6,7,8,9,10]
def multiply(number):
    return number * 5
"""function to multiply numbers by 5
    Expected input = [1,2,3,4,5,6,7,8,9,10]
    Expected output = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
"""
def transform(numbers):
    result =[]
    for number in numbers:
        result.append(multiply(number))
    return result

num =transform(list_numbers)


"""can be simplified as
    Expected input = [1,2,3,4,5,6,7,8,9,10]
    Expected output = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
"""
transform_numbers =[multiply(number) for number in list_numbers]




"""add 1 to any number greater than 25 otherwise subtract 1
Expected input = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
Expected output = [4, 9, 14, 19, 24, 31, 36, 41, 46, 51]
"""
transform_numbers_2= [number + 1 if number > 25 else number -1 for number in transform_numbers]





"""add 1 to any number greater than 25 else None
Expected input = [4, 9, 14, 19, 24, 31, 36, 41, 46, 51]
Expected output =[None, None, None, None, None, 30, 35, 40, 45, 50]
"""
filtered_numbers = [number -1 if number > 25 else None for number in transform_numbers_2]



list_numbers =[1,2,3,4,5,6,7,8,9,10]
def multiply(number):
    return number * 5
"""function to satisfy a condition
    Expected output = [False, False, False, False, False, True, True, True, True, True]
"""
def transform(numbers):
    result =[]
    for number in numbers:
        result.append(multiply(number))
    return result

num =transform(list_numbers)
print(num)
def filter_num(item):       
    return item > 25

transform_numbers =[multiply(number) for number in list_numbers]
transform_numbers_2= [number + 1 if number > 25 else number -1 for number in transform_numbers]
filtered_numbers = [filter_num(number) for number in transform_numbers_2]




list_numbers =[1,2,3,4,5,6,7,8,9,10]
def multiply(number):
    return number * 5
"""Using builtin to satisfy a condition then return the item
Expected output = [31, 36, 41, 46, 51]
"""
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




list_numbers =[1,2,3,4,5,6,7,8,9,10]
def multiply(number):
    return number * 5
"""Use built in with predicate function and don't return item
    Expected output = [31, 36, 41, 46, 51]
"""
def transform(numbers):
    result =[]
    for number in numbers:
        result.append(multiply(number))
    return result

num =transform(list_numbers)
print(num)
def filter_num(item):       
    return item > 25 

transform_numbers =[multiply(number) for number in list_numbers]
transform_numbers_2= [number + 1 if number > 25 else number -1 for number in transform_numbers]
filtered_numbers = [filter_num(number) for number in transform_numbers_2]
filtered_numbers_2 = list(filter(filter_num, transform_numbers_2))



"""Generator function to add"""
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

gen_result = gen_function(1)

"""Get the first figure out with the 'next'function, Expected output =1"""
print(next(gen_result))

"""Get the second figure out with the 'next'function, Expected output =2"""
print(next(gen_result))

"""Get the third figure out with the 'next'function, Expected output =11"""
print(next(gen_result))

"""Get the fourth figure out with the 'next'function, Expected output =21"""
print(next(gen_result))



numbers = [1,2,3,4,5,6,7,8,9] 
def find_number(numbers):
    for number in numbers:
        print(number)

def gen_find_number(numbers):
    for number in numbers:
        yield number

find_number(numbers)
gen_num = gen_find_number(numbers)
print(gen_num)

"""Get the first figure out with the 'next'function, Expected output =1"""
print(next(gen_num))

"""Get the second figure out with the 'next'function, Expected output =2"""
print(next(gen_num))

for item in gen_num:
    result = item + 5
"""Expected output = 8 9 10 11 12 13 14 """



"""Get values in a range, Expected output = 1 2 3 4"""
for item in range(1,5):
    result = next(gen_num)
    print(result)


#Time delay
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

