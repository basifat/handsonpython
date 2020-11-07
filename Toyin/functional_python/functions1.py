def unique_items():
    """
    Get unique item from a list
    Initialise an empty list lst = []
    Example input: [1,1,1,2,2,2,3,4,5,5]
    Expected output: [1,2,3,4,5]
    """
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique
items = [1,1,1,2,2,2,3,4,5,5]
a = unique_items()


def unique_items(items):
    unique = []
    """
    Modify so any argument can go through it
    Example input: [1,1,1,2,2,2,3,4,5,5]
    """
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique
duplicate= [1,1,1,2,2,2,3,4,5,5]
a = unique_items(duplicate)


"""to use a builtin function"""
duplicate= [1,1,1,2,2,2,3,4,5,5]
b = set(duplicate)


"""can be changed to a list"""
duplicate= [1,1,1,2,2,2,3,4,5,5]
b = list(set(duplicate))



def multiply_by_two(items):
    """list of items with every item multiplied by 2"""
    c = []
    for item in items:
        item = item * 2
        c.append(item)
    return c

a = unique_items(duplicate)
multiplied = multiply_by_two(a)



def multiply_item_by_two(item):
    return item * 2
    """
    Builtin fuction to get items multiplied by 2
    Introduce 'list' because Python 3 'map' returns an iterator 
    """
mapped_two = list(map(multiply_item_by_two, a))



def multiply_item_by_ten(item):
    return item * 10
    """Builtin function to multiply by 10"""
mapped_ten= list(map(multiply_item_by_ten, a))



def our_map(fn, item_list):
    """Higher order function that accept a function and a list"""
    new_list = []
    for item in item_list:
        mapped = fn(item)
        new_list.append(mapped)
    return new_list

our_map_result = our_map(multiply_item_by_ten, a)



def multiply_item_by_two(item):
    """Optimising, moving the function multiply_item_by_two(item) to the top"""
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



numbers = [0,1,2,3,4,5,6]
def greater_than_three(numbers):
    """
    Return a list of items with only items greater than 3
    Expected input =[0,1,2,3,4,5,6]
    Expected output = [4,5,6]
    """
    new_number = []
    for number in numbers:
        if number > 3:
            new_number.append(number)
    return new_number

filtered = greater_than_three(numbers)




def item_greater_than_three(item):
    if item > 3:
        return True
    """
    Another method
    Return a list of items with only items greater than 3
    Expected input =[0,1,2,3,4,5,6]
    Expected output = [4,5,6]
    """
def greater_than_three(numbers):
    new_number = []
    for number in numbers:
        if item_greater_than_three(number):
            new_number.append(number)
    return new_number

filtered = greater_than_three(numbers)



"""Return a list of items with only items greater than 3 with the builtin function 'filter'"""
filtered_2 = list(filter(item_greater_than_three, numbers))



def item_greater_than_three(item):
    return item > 3
    """optimising
    Return a list of items with only items greater than 3
    Expected input =[0,1,2,3,4,5,6]
    Expected output = [4,5,6]
    """
def greater_than_three(numbers):
    new_number = []
    for number in numbers:
        if item_greater_than_three(number):
            new_number.append(number)
    return new_number

filtered = greater_than_three(numbers)