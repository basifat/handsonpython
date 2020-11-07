def g_add(a,b):
    return a+ b


def hello_decorator(fn):
    """ Decorator function"""
    def wrapper():
        fn()
    return wrapper

@hello_decorator
def hello():
    return "we are in Hello function"

def hello_decorator_function(fn):
    """ invoking fn() twice"""
    def wrapper():
        fn()
        fn()
    return wrapper

@hello_decorator_function
def hello_fn():
    """ this will return the string twice"""
    return "we are in Hello function"

def addten(fn):
    def inner_function():
        return fn() + 10
    return inner_function


# @addten
# def threepoweroftwo():
#     return 3**3  ##returns 27

#print(threepoweroftwo())


    
# @add
# def threepoweroftwo():
#     return 3**3  ##returns 27

# print(threepoweroftwo())


def add(number):
    
    def plus2():

        def plus3():
            return number + 10

        return plus3

    return plus2


result = add(10)
#add(10) --> # plus2
#plus2() --> plus3
#plus3() --> 20
# print(result()())

#a -> b -> c -> d -> e


def add(*firstargs):
    
    def inner(fn):
        def wrapper(*nextargs):
            a, b = firstargs
            return fn(*nextargs) + a + b
        return wrapper
    return inner
    

def subtract():
    return 10-2

@add(10, 5)
def threepoweroftwo(first, second):
    return first**second

print(threepoweroftwo(3,3))

