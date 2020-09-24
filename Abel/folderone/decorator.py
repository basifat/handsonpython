def addten(fn):
    """ decorator function. """
    def inner_function():
        return fn() + 10
    return inner_function

@addten
def threepoweroftwo():
    """ returns the value of 3 **3 + the value from the decorator."""
    return 3**3  

def add(*firstargs):
    """ decorator function that accepts an arguement."""
    def inner(fn):
        def wrapper(*nextargs):
            a, b = firstargs
            return fn(*nextargs) + a + b
        return wrapper
    return inner

@add(10, 5)
def poweroftwo(first, second):
    """ returns the value of the first arguement raise to the power of the second argument."""
    return first**second
