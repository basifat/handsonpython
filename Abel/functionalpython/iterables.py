import time

def filter_items(numbers):
    """ 
    This functions return list of numbers greater than 3 and less than 7
    Example_input = [1, 2, 3, 4, 5, 6, 7, 8,9]
    output = [4,5,6]
    """
    new_numbers = []
    for number in numbers:
        if (number> 3) and (number < 7):
            new_numbers.append(number)
    return new_numbers

def divisible_by_two(numbers):
    """ finds and multiply numbers divisible by 2 by 100""" 
    times_two = []
    for number in numbers:
        if (number % 2 == 0):
            number *= 100 
        times_two.append(number)
        return times_two

def list_extension(numbers):
    """ this is a list comrenhension function that adds 2 to every number in the list"""
    numbers_updated = [number+2 for number in numbers]
    return numbers_updated


def multiply(number):
    return number * 5

def filter_num(items):
    """ returns items greater than 25 in an iterable"""
    return items > 25 


def transform(multiply,number_list):
    """ this function uses the 'multiply' function above to multiply each number in the list by 5"""
    transformed = [multiply(number) for number in number_list]
    return transformed

def inbuilt_filter(filter_num, transformed):

    filtered_numbers = list(filter(filter_num, transformed))
    return filtered_numbers


def gen_find_numbers(numbers):
    """ 
    This Generator function return next item in an iterable until the iterable is exausted
    Sample invocation:
    gen_result = gen_find_numbers(numbers)
    print(next(gen_result))

    """
    for number in numbers:
        yield number

number_list = [ 2,4,6,8]
gen_result = gen_find_numbers(number_list)


def gen_timer():
    """ 
    returns a number from the generator function every 2 seconds
    Example usage: the generator function 'gen_find_numbers' is invoked by giving it a list as an arguement
    gen_result = gen_find_numbers(number_list),
    the gen_result is then passed to the variable 'result' in the gen_timer function.
    
    """
    result =[]
    
    def extract_value():
        try:
            time.sleep(2)
            next_item = next(gen_result)
            return next_item
        except StopIteration as e:
            raise e
    
    while True:
        try:
            item= extract_value()
            result.append(item)
        except:
            return result, "generator exhausted"
        
    

    









