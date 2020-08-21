# Write a function that accepts a list of numbers and returns the first number greater than 7
# numbers = [3,6,5,4,9,18,2,1,0,28]
# output = 9
# iterate through the list
# find the first no.> 7
# break the loop once no. is found


# 3  > 28 , No
# 3 > 18, No
# 6 > 28, No
# 6 > 18, No
# 3 ,6 ,5 ,4 ,9 ,19
#
#
#

numbers = [3,6,5,4,9,2,1,0,28, 19, 32]
def number_greater_than_seven(items):
    item_list = []
    for item in items:
        if item > 28:
            item_list.append(item)
        if item > 18:
            item_list.append(item)
    return item_list
        
seven = number_greater_than_seven(numbers)
print(seven)

#Reducing functions
#Filtering functions  [1,2,3,4,5] ==> [4,5]
#Mapping function [1,2,3,4,5] ==> [1,4,9,16,25]
#Summing function [1,2,3,4,5] ==> 15

numerals = [1,2,3,4,5]

def sum_of_list(items):
    total = 0
    for item in items:
        total = total + item 
    return total
    
total = sum_of_list(numerals)
print(total)

total_builtin = sum(numerals)
print(total_builtin)


#Write a function that returns True if all the elements in a list have a value that is equal to 'True'
#Write a False if any of the elements in a list has a value that is equal to 'False'

list_all=[True, True, True]
# list_all_neg=[True, True, False]
exp_list = [1, 2, 3]
exp_result  = 3 in exp_list
# print(exp_result)

def all_true(items):
    """ Returns True using list membership check"""
    return False not in items


def all_true_2(items):
    """ Returns True using iteration if all elements in blah blah are True"""
    for item in items:
        if item == True:
            pass
        else:
            return False
    return True
            

is_all_true = all_true(list_all)
print(is_all_true)

# is_all_true_builtin =all(list_all)
# print(is_all_true_builtin)

    
