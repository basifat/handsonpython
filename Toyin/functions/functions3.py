#thursday 20/08/2020
# #Write a function that accepts two arguments a and b, then adds both together
def addition(a,b):
    """ Sums two integers and returns the value"""
    return a+b
result=addition(2,3)
print(result)
#output is 
#5


## Definning a partial function
# First argument a will be used later in summation by function comp_addtion
def partial_addition(a):
    """Higher order function that returns comp_addition"""
    def comp_addition(b):
        return a+b 
    return comp_addition
partial_result=partial_addition(2)
print(partial_result)
#output is
#<function partial_addition.<locals>.comp_addition at 0x7fca0d5675e0>

#so we amended the code to be
#Referencing addition with a different name
def partial_addition(a):
    """Higher order function that returns comp_addition"""
    def comp_addition(b):
        return a+b 
    return comp_addition
copy_addition = addition
copy_result = copy_addition(2,3)
print(copy_result)
#output is 5
#it returned same result as above
#higher function, u return a function or accept a function as an argument and u do something to it.
#higher order function give u an ability to have closure

##############*******************
# copy_addition = addition
# copy_result = copy_addition(2,3,4) #this will not run because
#print(copy_result)
#the function that was declared only has 2 argument so we can't call 3 argument
#********************************************

#another instance
def partial_addition(a):
    """Higher order function that returns comp_addition"""
    def comp_addition(b):
        return a+b 
    return comp_addition
partial_result=partial_addition(2)
final_result=partial_result(3)
print(final_result)
#this will still print 5 because 'partial result' has 2 and now 3 added to it

#************
def partial_addition(a):
    """Higher order function that returns comp_addition"""
    def comp_addition(b):
        d = a+b

        def multiply(c):
            return d * c
        return multiply

    return comp_addition
copy_addition = addition
copy_result = copy_addition(2,3)
partial_result=partial_addition(2)
final_result=partial_result(3)
print(final_result)
a = partial_result(1)
b = a(2)
c = b(3)
print(c)
#output is 9


#Example 2
#Have a function that splits a word with hypen ("Hello-Tunde") into two
def split_text(word):
    a = word.split('-') 
    print(a)

split_text('Hello-Tunde')
#output is ['Hello', 'Tunde']

#to return 'Hello-' ###################
def split_text(word):
    a = word.split('T') 
    print(a)
split_text('Hello-Tunde')
#output is ['Hello-', 'unde']

#then we know the below will do the split
def split_text(word):
    a = word.split('T') 
    d = a[0]
    print(d)
split_text('Hello-Tunde')
#output is Hello-

#can also be 
def split_text(word):
    a = word.split('T') 
    return a[0]
    
word = split_text('Hello-Tunde')
print(word)
#output is Hello-

#Example
# transform each name to start with Hello- 
#define a new function
names = ["Tunde", "Ray", "Jay", "Mo"]
#output expected =["Hello-Tunde", "Hello-Ray"...]
def split_text(word):
    a = word.split('T') 
    d = a[0]

    def cooler_names(list_names):
        cool_names = []
        for name in list_names:
            result = d+name
            cool_names.append(result)
        return cool_names
        
    return cooler_names

result_function = split_text("Hello-Tunde")
#print(result_function) #output is <function split_text.<locals>.cooler_names at 0x7f96f4755550>
coolio = result_function(names)
print(coolio)
#output is ['Hello-Tunde', 'Hello-Ray', 'Hello-Jay', 'Hello-Mo']









