# write a function that returns unique items of a list
# Task breakdown:
# 1.example output = [1,2,3,4,5]
# 2.loop through the number list
# 3. create new list and add numbers to the list if not already in the list

def unique_items(duplicate):
    """ get unique times from a list"""
    unique = []
    for number in duplicate:
        if number not in unique:
            unique.append(number)
    return unique

duplicate = [1,1,1,2,2,2,3,3,4,5]
unique_duplicate = unique_items(duplicate)
print(unique_duplicate)

# using inbuilt set to remove duplicate from list
a = list(set(duplicate))
print(a)

# write a function that returns a list of items and the items now multiplied by 2
def multiply_item_by_two(item):
    """ multiply item by 2 """
    return item * 2


def multiply_by_two(items):
    c = []
    for item in items:
        item=multiply_item_by_two(item)
        c.append(item)
    return c
        

b = unique_items(duplicate)
multiplied_number =multiply_by_two(b)
print(multiplied_number)


mapped= map(multiply_item_by_two, b)
result =list(mapped)
print(result)

# higher order fucntion
def our_map(fn, items):
    map_new = []
    for item in items:
        maped=fn(item)
        map_new.append(maped)
    return map_new

d = our_map(multiply_item_by_two, b)
print(d)

number_list = [2,4,3,1,6,8,9]

#write a function that return a list of items greater than 3
def greater_than_three(num):
    """ returns item greater than 3 """
    return num > 3
        
    
def items_greater_than_three(items):
    item_list = []
    for item in items:
        if greater_than_three(item):
            item_list.append(item)
    return item_list


greather=items_greater_than_three(number_list)
print(greather)

# using python in-built function to filter items > 3
filter_2 = filter(greater_than_three, number_list)
final_filter = list(filter_2)
print(final_filter)

