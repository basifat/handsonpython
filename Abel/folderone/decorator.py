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
