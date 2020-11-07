#21/08/2020********************
# # #contd from functions_three
names = ["Tunde", "Ray", "Jay", "Mo"]
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
coolio = result_function(names)
print(coolio)


names = ["Tunde", "Ray", "Jay", "Mo"]
animals = ['Dog', 'Cat', 'Pig']
automobile = ['Car', 'Bicycle', 'Tractor']


tr_names = result_function(names)
tr_animals = result_function(animals)
tr_automobile = result_function(automobile)
print(tr_names)
print(tr_animals)
print(tr_automobile)
#output is 
# ['Hello-Tunde', 'Hello-Ray', 'Hello-Jay', 'Hello-Mo']
# ['Hello-Dog', 'Hello-Cat', 'Hello-Pig']
# ['Hello-Car', 'Hello-Bicycle', 'Hello-Tractor']

#another example
def transform_list(word, lst):
    new_list = []
    for item in lst:
        result= word + item
        new_list.append(result)
    return new_list

tr_names_2 = transform_list("Hello-", names)
tr_animals_2 = transform_list("Hello-", animals)
tr_automobile_2 = transform_list("Hello-", automobile)
print(tr_names_2)
print(tr_animals_2)
print(tr_automobile_2)
## output is ['Hello-Tunde', 'Hello-Ray', 'Hello-Jay', 'Hello-Mo']
#['Hello-Dog', 'Hello-Cat', 'Hello-Pig']
[#'Hello-Car', 'Hello-Bicycle', 'Hello-Tractor']


#accept a function and do something withit
def subtract(a, b):
    return a - b # 10 -7  

def do_subtract(num, alg, fn):
        return fn(num, alg) # subtract(10, 7)

result = do_subtract(10, 7, subtract)
print(result)
#output is 3
#1#fn(10, 7) #subtarct(10, 7) => 3
#2#do_subtract(10, 7, subtract) => 3

#can even do the below
def subtract(a, b):
    return a - b # 10 -7  

def do_subtract(num, alg, fn):
        return fn(num, alg)*3 # subtract(10, 7)*3

result = do_subtract(10, 7, subtract)
print(result)
#output is 9
#higher order function is something that accept a function as an argumnetor or returns a functionas an argument


#Decorator function*****************
# def hello_decorator(fn):
    def wrapper():
        fn()
    return wrapper

@hello_decorator
def hello():
    print("we are in Hello function")
hello()
#output is
#we are in Hello function

#and adding 'fn()' twice
def hello_decorator(fn):
    def wrapper():
        fn()
        fn()
    return wrapper

@hello_decorator
def hello():
    print("we are in Hello function")
hello()
#output is
#we are in Hello function
#we are in Hello function

#if we take the decorator away and run it
def hello_decorator(fn):
    def wrapper():
        fn()
        fn()
    return wrapper

#@hello_decorator
def hello():
    print("we are in Hello function")
hello()
#output is
#we are in Hello function

#adding some 'print' statements and taking the decorator away
def hello_decorator(fn):
    def wrapper():
        print("i will do some initial work") 
        fn()
        fn()
        print("i will do some after work") 
    return wrapper

#@hello_decorator
def hello():
    print("we are in Hello function")
hello()
#output is 
#we are in Hello function


#adding some 'print' statements and the decorator
def hello_decorator(fn):
    def wrapper():
        print("i will do some initial work")
        fn()
        fn()
        print("i will do some after work") 
    return wrapper

@hello_decorator
def hello():
    print("we are in Hello function")
hello()
#output is 
#i will do some initial work
#we are in Hello function
#we are in Hello function
#i will do some after work

#remove one of the fn() statements
def hello_decorator(fn):
    def wrapper():
        print("i will do some initial work") # launch a web browser
        fn()
        print("i will do some after work") # terminate a web browser
    return wrapper

@hello_decorator
def assert_1():
    assert 1 ==1
    print("we are in Hello function")

@hello_decorator
def assert_2():
    assert 2 ==2
    print("we are in Hello function")

@hello_decorator
def assert_3():
    assert 3 ==3
    print("we are in Hello function")

assert_3()
#output is 
#i will do some initial work
#we are in Hello function
#i will do some after work

def login(fn):

    def wrapper():
        #some.login(user)
         #clear cache
         # if user not loggged:
          # kick user out
        pass
    return wrapper

@login
def send_user_to_dashboard_page():
     # show user dahsboard
     # redirect user to account page settings
    pass
#output is 
# i will do some initial work
# we are in Hello function
# i will do some after work

