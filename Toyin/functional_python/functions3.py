def addition(a,b):
    """ Sums two integers and returns the value
    Expected output = 5
    """
    return a+b
result=addition(2,3)



def partial_addition(a):
    """Higher order function that returns comp_addition"""
    def comp_addition(b):
        return a+b 
    return comp_addition
partial_result=partial_addition(2)



def partial_addition(a):
    """Higher order function that returns comp_addition
    Expected output = 5
    """
    def comp_addition(b):
        return a+b 
    return comp_addition
copy_addition = addition
copy_result = copy_addition(2,3)



def partial_addition(a):
    """Higher order function that returns comp_addition
    Expected output = 5
    """
    def comp_addition(b):
        return a+b 
    return comp_addition
partial_result=partial_addition(2)
final_result=partial_result(3)



def partial_addition(a):
    """Higher order function that returns comp_addition
    Expected output = 9
    """
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
c = a(3)



def split_text(word):
    """function that splits a word with hypen
    Expected output = ['Hello', 'Tunde']
    """
    a = word.split('-') 
    print(a)

split_text('Hello-Tunde')



def split_text(word):
    """function that splits a word with hypen
    Expected output = ['Hello-', 'unde']
    """
    a = word.split('T') 
    print(a)
split_text('Hello-Tunde')



def split_text(word):
    """function that splits a word with hypen
    Expected output = Hello-
    """
    a = word.split('T') 
    d = a[0]
    print(d)
split_text('Hello-Tunde')



def split_text(word):
    """function that splits a word with hypen
    Expected output = Hello-
    """
    a = word.split('T') 
    return a[0]
    
word = split_text('Hello-Tunde')



names = ["Tunde", "Ray", "Jay", "Mo"]
def split_text(word):
    """transform each name to start with Hello- 
    Expected Input = ["Tunde", "Ray", "Jay", "Mo"]
    Expected Output = ['Hello-Tunde', 'Hello-Ray', 'Hello-Jay', 'Hello-Mo']"""
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
coolio = result_function(names)













