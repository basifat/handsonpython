# Write a function that returns a list containing only unique items from a list
# Example output = [1,2,3,4,5]

#Tasks to produce result
#1. loop through the item list
#2. create a new list and add numbers to the new list if not already in the list

def unique_items(items):
    """Gets unique item from a list"""
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

            
duplicate= [1,1,1,2,2,2,3,4,5,5]
a = unique_items(duplicate)
print(a)

## Uses python builtin set to elimnate duplicates
b = set(duplicate)
print(b)

def multiply_item_by_two(item):
    """Helper function for multiplying by 2"""
    return item * 2

def multiple_item_by_ten(item):
    return item * 10

#Write a function that returns a list of items with every item now multiplied by 2
def multiply_by_two(items):
    c = []
    for item in items:
        item = multiply_item_by_two(item)
        c.append(item)
    return c

a = unique_items(duplicate)
multiplied = multiply_by_two(a)
print(multiplied)

mapped = map(multiply_item_by_two, a)
mapped_2 = map(multiple_item_by_ten, a)
print(mapped)
print(mapped_2)


#Higher order function
def our_map(fn, item_list):
    new_list = []
    for item in item_list:
        mapped = fn(item)
        new_list.append(mapped)
    return new_list

our_map_result = our_map(multiple_item_by_ten, a)
print(our_map_result)


#Write a function that returns a list of items with only items greater than 3
# output = [4,5,6]

numbers = [0,1,2,3,4,5,6]
4 > 3 # True
1 > 3 # False

def item_greater_than_three(item):
    return item > 3

def greater_than_three(numbers):
    new_number = []
    for number in numbers:
        if item_greater_than_three(number):
            new_number.append(number)
    return new_number

filtered = greater_than_three(numbers)
print(filtered)


filtered_2 = filter(item_greater_than_three, numbers)
print(filtered_2)

#Write a function that returns a list of items with only items greater than 3
# output = [4,5,6]

def items_greater_than_three(items):
    #decalres an empty list
    for item in items:
        # appends item to list
    # returns the list




