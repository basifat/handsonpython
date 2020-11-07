# Functional programming pipeline

# Function Generators

# Funtion typings

# Aliasing functions

# Arbitrary keyword arguments for a function

# Unpacking
import time
from functions_day_5_helper import g_add as sum_total



list_numbers =[1,2,3,4,5,6,7,8,9,10]

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
# filtered_numbers = [filter_num(number) for number in transform_numbers_2]
filtered_numbers_2 = filter(filter_num, transform_numbers_2)
#[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#[4, 9, 14, 19, 24, 31, 36, 41, 46, 51]
# print(transform_numbers_2)
# print(transform_numbers)
# # print(filtered_numbers)
# print(filtered_numbers_2)


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
gen_result = gen_function(1)
#print(gen_result)

# print(next(gen_result))
# print(next(gen_result))
# print(next(gen_result))
# print(next(gen_result))

#500,000 
#card_transactions = [1,2,3] # 500_transactions
# for item in card_transactions:
numbers = [1,2,3,4,5,6,7,8,9] # 10 million transations 
def find_number(numbers):
    for number in numbers:
        print(number)

def gen_find_number(numbers):
    for number in numbers:
        yield number

find_number(numbers)
gen_num = gen_find_number(numbers)
print(gen_num)
# print(next(gen_num))
# print(next(gen_num))

#numbers = [1,2,3,4,5,6,7,8,9] 
# def gen_timer():

#     while True:
#         time.sleep(1)
#         try:
#             result = next(gen_num) # [100000]
#             print(result)
#         except StopIteration:
#             print("generator is exhausted")
#             return 
# gen_timer()

# for item in gen_num:

#     result = item + 5
#     print(result)
# def subtract_2(age: int, salary:int) -> int:
#     # """
#     # Subtracts age from salary
#     # """
#     return age - salary


# def f(num1: int, my_float: float = 3.5) -> float:
#     return num1 + my_float


# sub = f(22)
# print(sub)

# Write a function that have one parameter that collects as many arguments as possible
#Call the fucntion three time with different arguments

dico = {"a": 10, "b": 20}
print(dico)


def manufacture_zero(version, iphone = None, samsung = None, motorola = None):
    return version, iphone, samsung, motorola

def manufacture_phones(*args,**kwargs):
    return (args, kwargs)

result = manufacture_phones(10,iphone = 'xmax',samsung = 'g9')
print(result)

result = manufacture_phones(iphone = 'xmax',samsung = 'g9', motorola = 'b5', lg="lgx9")
print(result)







    



