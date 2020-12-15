def unique_items(duplicate):
    """ 
    Gets unique items of a list.
    Example input = [1,1,1,2,2,2,3,3,4,5]
    Example output = [1,2,3,4,5]
    create new list and add numbers to the list if not already in the list
    
    """
    unique = []
    for number in duplicate:
        if number not in unique:
            unique.append(number)
    return unique

def inbuilt_remove_duplicate(duplicate):
    """ using inbuilt set to remove duplicate from list"""
    a = list(set(duplicate))
    return a

def multiply_item_by_two(item):
    """ multiply item by 2 """
    return item * 2

def multiply_by_two(items):
    """ returns a list of numbers multiplied by 2"""
    c = []
    for item in items:
        item=multiply_item_by_two(item)
        c.append(item)
    return c
        
def our_map(fn, items):
    """ higher order fucntion that returns list of mapped items """
    map_new = []
    for item in items:
        maped=fn(item)
        map_new.append(maped)
    return map_new

def greater_than_three(num):
    """ returns item greater than 3 """
    return num > 3
            
def items_greater_than_three(items):
    """ returns list of items greater than 3"""
    item_list = []
    for item in items:
        if greater_than_three(item):
            item_list.append(item)
    return item_list

def inbuilt_filter(fn, number_list):
    """ 
    using python in-built 'filter' to return items greater than 3 
    Example input = [3,4,5,6,8,7]
    Example output = [4,5,6,8,7]
    
    """
    filter_result = filter(fn, number_list)
    final_filter = list(filter_result)
    return final_filter

def partial_addition(a):

    def comp_addition(b):
        d = a+b 
        def multiply(c):
            return d * c
        return multiply
    return comp_addition


def split_text(word):
    """ 
    this function overloading returns a list containing items with attatched 
    prefix.
    names = ["Boris", "Ray", "Jay", "Mo"]
    result = split_text("Hello-Titus")
    attached = result(names)
    sample out_put = ["Hello-Boris", "Hello-Ray", "Hello-Jay", "Hello-Mo"] 
    
    """
    a = word.split('T') 
    d = a[0]

    def cooler_names(list_names):
        cool_names = []
        for name in list_names:
            result = d+name
            cool_names.append(result)
        return cool_names
        
    return cooler_names

def transform_list(word, lst):
    """ returns the same output as the above function."""
    new_list = []
    for item in lst:
        result= word + item
        new_list.append(result)
    return new_list

def manufacture_phone(*args,**kwargs):
    """
    This function takes any number of positional argument and key word arguement.
    Example:
    new_phones =manufacture_phone(10, 20,iphone="5x", samsung="S10", tecno="g4").
    
    """
    return args,kwargs



