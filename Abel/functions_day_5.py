# funtional programing pipeline
# functions generator 
# functions type hints 
# functions Aliasing
# Arbitriary keyword argument for a function
from functions_extended import addition as sum_total
import time
def multiply(number):
    return number * 5

def filter_num(items):
    return items > 25 

number_list = [1,2,3,4,5,6,7,8,9,10]

# list comprehension
transformed = [multiply(number) for number in number_list]
print(transformed)

# add 1 to number > 25 else subtract 1 from numbers
# output = [4, 9, 14, 19, 24, 31, 36, 41, 46, 51]
transformed_num =[number + 1 if number > 25 else number - 1 for number in transformed]
print(transformed_num)

filtered_numbers = list(filter(filter_num, transformed_num))
print(filtered_numbers)

def find_numbers(numbers):
    for number in numbers:
        print(number)

def gen_find_numbers(numbers):
    for number in numbers:
        yield number

find_numbers(number_list)
gen_result = gen_find_numbers(number_list)
#print(next(gen_result))

def gen_timer(): #return a number from the generator every 5 seconds
    while True:
        try:
            time.sleep(5)
            result = next(gen_result)
            print(result)
        except StopIteration:
            print(" genarator exusted")
            return

#gen_timer()

# write a function that have one parameter and accepts many argument
# call the the function three times with different argument

def manufacture_phone(*args,**kwargs): # this means i can add any no of positional argument $ kwargs when the function is called

    return args,kwargs

new_phones =manufacture_phone(10, 20,iphone="5x", samsung="S10", tecno="g4")
print(new_phones)
