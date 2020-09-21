# Example1: Write a function that accepts a list of numbers and returns the first number greater than 7
# numbers = [3,6,5,4,9,18,2,1,0,28]
# output = 9
#define a function
# iterate through the list
# find the first number greater than 7
# break the loop once the number is found

numbers = [3,6,5,4,9,18,2,1,0,28]
def number_greater_than_seven(items):
    for item in items:
        if item > 7:
            break
    return item
        
seven = number_greater_than_seven(numbers)
print(seven)
#output is 9

#can also be done as below which is to get the first and leave, do not need to return to find anything else
def number_greater_than_seven(items):
    for item in items:
        if item > 7:
            return item
        
seven = number_greater_than_seven(numbers)
print(seven)
#output is 9

#because we used the break statement, we immediately left after we got the first one greater than 7
#we then return and printed the item 9
def number_greater_than_seven(items):
    for item in items:
        if item > 7:
            print(item)
            break
    return item
        
seven = number_greater_than_seven(numbers)
print(seven)
#output is 
#9
#9


# Trying the return early 
#this returns the list
numbers = [3,6,5,4,9,18,2,1,0,28]
def number_greater_than_seven(items):
    for item in items:
        print(item)
        if item > 7:
            break    
    return item
        
seven = number_greater_than_seven(numbers)
print(seven)
#output was 
#3
#6
#5
#4
#9
#9


#the below shows an instance that might not be easy to get out of the loop
numbers = [3,6,5,4,9,18,2,1,0,28]
def number_greater_than_seven(items):
    result = 0
    for item in items:
        print(item)
        if item > 7:
            result = item   
    return result
        
seven = number_greater_than_seven(numbers)
print(seven)
#output is 
#6
#5
#4
#9
#18
#2
#1
#0
#28
#28


#Write a function that accepts a list of numbers and returns 
# the first number greater than 7 and 18
numbers = [3,6,5,4,9,18,2,1,0,28]
def number_greater_than_seven(items):
    for item in items:
        if item > 7:
            return "found a number greater than seven"
        if item > 18:
            return "found a number greater than eighteen"
        
seven = number_greater_than_seven(numbers)
print(seven)
#output is 
#found a number greater than seven
#it stopped because of the return statement whenever the return statement
# is true it will never get to the next part and never got to the next iteration


#another example
numbers = [3,6,5,4,9,19,2,1,0,28,32]
# 3  > 28 , No
# 3 > 18, No
# 6 > 28, No
# 6 > 18, No
# 3 ,6 ,5 ,4 ,9 ,19
def number_greater_than_seven(items):
    for item in items:
        if item > 28:
            return "found a number greater than seven"
        if item > 18:
            return "found a number greater than eighteen"
        
seven = number_greater_than_seven(numbers)
print(seven)
#output is 
#found a number greater than eighteen
#because that is the first true statement and it will stop because of the return statement

#another example
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
#output is 
#[28, 19, 32, 32]
#because this time it will iterate through the list to give us all the
# true statement and then return the whole list
#multiply conditions were satisfied

########Reducing functions******************
#Filtering functions  [1,2,3,4,5] , if we want to filter things greater than 3 ==> [4,5]
#Mapping function [1,2,3,4,5], mapp this to their squares==> [1,4,9,16,25]
#Summing function [1,2,3,4,5] ==> 15. no data type

#example 1: write a function that sums the below
numerals = [1,2,3,4,5]

def sum_of_list(items):
    total = 0
    for item in items:
        total = total + item 
    return total
    
total = sum_of_list(numerals)
print(total)
#output is 15

#to use the builtin function
numerals = [1,2,3,4,5]
total_builtin = sum(numerals)
print(total_builtin)
#output is 15
#'sum' is a builtin function without having to write a user defined function


#*********************
#Example
#Write a function that returns True if all the elements in a list have a value that is equal to 'True'
##Write a False if any of the elements in a list has a value that is equal to 'False'

list_all=[True, True, True]
# list_all_neg=[True, True, False]

#Write a function that returns True if all the elements in a list have a value that is equal to 'True'
list_all=[True, True, True]
def all_true(items):
    for item in items:
        if item == True:
            print(item)
            pass
        
is_all_true = all_true(list_all)
print(is_all_true)
#output is 
#True
#True
#True
#None
#the printing is happening in the function(before the 'pass')
#None is because of the last print statement is expecting to print the 
#return value that will be stored in 'is_all_True' but we've not stored anything there yet

#and to include the return value
def all_true(items):
    for item in items:
        if item == True:
            print(item)
            pass
        else:
            return False
            
is_all_true = all_true(list_all)
print(is_all_true)
#output is 
#True
#True
#True
#None

def all_true(items):
    """ Returns True using iteration if all elements is True"""
    for item in items:
        if item == True:
            print(item)
            pass
        else:
            return False
    return True
            
is_all_true = all_true(list_all)
print(is_all_true)
#output is
#True
#True
#True
#True
#for this we will never get to the else block because nothing satisfies it. 
# the for loop is done after the 3rd 'True' and we just to the 'return True'

#included a 'False' into the list 
list_all=[True, False,True, True]
def all_true(items):
    for item in items:
        if item == True:
            print(item)
            pass
        else:
            return False
    return True
            
is_all_true = all_true(list_all)
print(is_all_true)
#output is 
#True
#False
#the Else block is returning 'False', it's not printing 'False'

#another instance
#if the 'return False' is changed to Print(False)
list_all=[True, False,True, True]
def all_true(items):
    for item in items:
        if item == True:
            print(item)
            pass
        else:
            print(False)
    return True
            
is_all_true = all_true(list_all)
print(is_all_true)
#output is 
#True
#False
#True
#True
#True

# when the print(item) is taken out and the print(False) is changed to 'return false'
list_all=[True, False,True, True]
def all_true(items):
    for item in items:
        if item == True:
            pass
        else:
            return False
    return True
            
is_all_true = all_true(list_all)
print(is_all_true)
#output is 
#False 

#removing the 'False' from the list
list_all=[True, True, True]
def all_true(items):
    for item in items:
        if item == True:
            pass
        else:
            return False
    return True
            
is_all_true = all_true(list_all)
print(is_all_true)
#output is
#True

#using the builtin function
is_all_true_builtin =all(list_all)
print(is_all_true_builtin)
#output is
#True

#if we change the third item to 'False'
list_all=[True, True, False]
def all_true(items):
    for item in items:
        if item == True:
            pass
        else:
            return False
    return True
#using the builtin function
is_all_true_builtin =all(list_all)
print(is_all_true_builtin)
#output is
#False

#how to check for list membership
# list_all_neg=[True, True, False]
exp_list = [1, 2, 3]
exp_result  = 3 in exp_list
print(exp_result)
#output is 
#True

#with this we can amend our code as below
list_all=[True, True, False]
def all_true(items):
    return True in items
is_all_true = all_true(list_all)
print(is_all_true)
#output is 
#True
#which is not correct so we will do the below

list_all=[True, True, False]
def all_true(items):
    return False not in items
is_all_true = all_true(list_all)
print(is_all_true)
#output is 
#False

list_all=[True, True, True]
def all_true(items):
    return False not in items
is_all_true = all_true(list_all)
print(is_all_true)
#output is 
#True


