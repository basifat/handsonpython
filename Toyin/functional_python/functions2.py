numbers = [3,6,5,4,9,18,2,1,0,28]
def number_greater_than_seven(items):
    """
    function that accepts a list of numbers and returns the first number greater than 7
    Example input = [3,6,5,4,9,18,2,1,0,28]
    Example output = 9
    """
    for item in items:
        if item > 7:
            break
    return item
        
seven = number_greater_than_seven(numbers)



def number_greater_than_seven(items):
    """
    function that accepts a list of numbers to get the first number greater than 7 and leave
    Do not need to return to find anything else
    Example input = [3,6,5,4,9,18,2,1,0,28]
    Example output = 9
    """
    for item in items:
        if item > 7:
            return item
        
seven = number_greater_than_seven(numbers)



def number_greater_than_seven(items):
    """
    function that accepts a list of numbers and returns the first number greater than 7, using 'break'
    Example input = [3,6,5,4,9,18,2,1,0,28]
    Example output = 9
    """
    for item in items:
        if item > 7:
            print(item)
            break
    return item
        
seven = number_greater_than_seven(numbers)



numbers = [3,6,5,4,9,18,2,1,0,28]
def number_greater_than_seven(items):
    """
    function that accepts a list of numbers and returns the number greater than 7, using the return early
    Example input = [3,6,5,4,9,18,2,1,0,28]
    Example output = a list; 3, 6, 5, 4, 9, 9
    """
    for item in items:
        print(item)
        if item > 7:
            break    
    return item
        
seven = number_greater_than_seven(numbers)



numbers = [3,6,5,4,9,18,2,1,0,28]
def number_greater_than_seven(items):
    """
    An instance that might not be easy to get out of the loop
    function that accepts a list of numbers and returns the number greater than 7, using the return early
    Example input = [3,6,5,4,9,18,2,1,0,28]
    Example output = a list; 3,6,5,4,9,18,2,1,0,28,28
    """
    result = 0
    for item in items:
        print(item)
        if item > 7:
            result = item   
    return result
        
seven = number_greater_than_seven(numbers)



def number_greater_than_seven(items):
    """
    Function that accepts a list of numbers and returns 
    the first number greater than 7 and 18
    whenever the return statement is true, it will never get to the next iteration
    Expected Input = [3,6,5,4,9,18,2,1,0,28]
    Expected output = found a number greater than seven
    """
    for item in items:
        if item > 7:
            return "found a number greater than seven"
        if item > 18:
            return "found a number greater than eighteen"
        
seven = number_greater_than_seven(numbers)



numbers = [3,6,5,4,9,19,2,1,0,28,32]
def number_greater_than_seven(items):
    """
    Function that accepts a list of numbers and returns 
    the first number greater than 18
    it will stop after the first true statement. 
    Expected Input = [3,6,5,4,9,19,2,1,0,28,32]
    Expected output = found a number greater than eighteen
    """
    for item in items:
        if item > 28:
            return "found a number greater than seven"
        if item > 18:
            return "found a number greater than eighteen"
        
seven = number_greater_than_seven(numbers)



numbers = [3,6,5,4,9,2,1,0,28, 19, 32]
def number_greater_than_seven(items):
    """
    Function that accepts a list of numbers and returns 
    the numbers greater than 28 and 18
    This will iterate through the list 
    Expected Input = [3,6,5,4,9,2,1,0,28, 19, 32]
    Expected output = [28, 19, 32, 32]
    """
    item_list = []
    for item in items:
        if item > 28:
            item_list.append(item)
        if item > 18:
            item_list.append(item)
    return item_list
        
seven = number_greater_than_seven(numbers)



numerals = [1,2,3,4,5]
def sum_of_list(items):
    """
    Function that sum
    Expected Input = [1,2,3,4,5]
    Expected Output = 15
    """
    total = 0
    for item in items:
        total = total + item 
    return total
    
total = sum_of_list(numerals)



numerals = [1,2,3,4,5]
"""use the builtin function
Expected Input = [1,2,3,4,5]
Expected Output = 15
"""
total_builtin = sum(numerals)



list_all=[True, True, True]
def all_true(items):
    """
    Function that returns True if all the elements in a list have a value that is equal to 'True'
    Expected Input = [True, True, True]
    Expected Output = True True True None
    """
    for item in items:
        if item == True:
            print(item)
            pass
        
is_all_true = all_true(list_all)



def all_true(items):
    """
    Function that returns True if all the elements in a list have a value that is equal to 'True' using a return
    Expected Input = [True, True, True]
    Expected Output = True True True None
    """
    for item in items:
        if item == True:
            print(item)
            pass
        else:
            return False
            
is_all_true = all_true(list_all)



def all_true(items):
    """ Returns True using iteration if all elements is True
    Expected Input = [True, True, True]
    Expected Output = True True True True
    """
    for item in items:
        if item == True:
            print(item)
            pass
        else:
            return False
    return True
            
is_all_true = all_true(list_all)



list_all=[True, False,True, True]
def all_true(items):
    """
    Function that returns True if all the elements in a list have a value that is equal to 'True' using a return False
    Expected Input = [True, False,True, True]
    Expected Output = True False
    """
    for item in items:
        if item == True:
            print(item)
            pass
        else:
            return False
    return True
            
is_all_true = all_true(list_all)



list_all=[True, False,True, True]
def all_true(items):
    """
    Function that returns True if all the elements in a list have a value that is equal to 'True' using a print(False)
    Expected Input = [True, False,True, True]
    Expected Output = True False True True True
    """
    for item in items:
        if item == True:
            print(item)
            pass
        else:
            print(False)
    return True
            
is_all_true = all_true(list_all)



list_all=[True, False,True, True]
def all_true(items):
    """
    Function that returns True if all the elements in a list have a value that is equal to 'True' 
    when the print(item) is taken out and the print(False) is changed to 'return false'
    Expected Input = [True, False,True, True]
    Expected Output = False
    """
    for item in items:
        if item == True:
            pass
        else:
            return False
    return True
            
is_all_true = all_true(list_all)
 


list_all=[True, True, True]
def all_true(items):
    """
    Function that returns True if all the elements in a list have a value that is equal to 'True' 
    Expected Input = [True, True, True]
    Expected Output = True
    """
    for item in items:
        if item == True:
            pass
        else:
            return False
    return True
            
is_all_true = all_true(list_all)



"""Function that returns True if all the elements in a list have a value that is equal to 'True' """
is_all_true_builtin =all(list_all)



"""check for list membership"""
exp_list = [1, 2, 3]
exp_result  = 3 in exp_list



list_all=[True, True, False]
def all_true(items):
    """check for list membership
    Expected Input = [True, True, False]
    Expected Output = False
    """
    return False not in items
is_all_true = all_true(list_all)



list_all=[True, True, True]
def all_true(items):
    """check for list membership
    Expected Input = [True, True, True]
    Expected Output = True
    """
    return False not in items
is_all_true = all_true(list_all)



