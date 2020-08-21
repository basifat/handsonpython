#Write a function that accepts two arguments a and b, then adds both together
def addition(a,b):
    """ Sums two integers and returns the value"""
    return a+b
result=addition(2,3)
# print(result)

## Definining a partial function
# First argument a will be used later in summation by 
# function comp_addtion

def partial_addition(a):
    """Higher order function that returns comp_addition"""

    #things in happening here
    #keep that information
    
    def comp_addition(b):
        d = a+b #reading file from
        # d = fetch_erver_file()
        
        def multiply(c):
            #modify_user_access()
            return d * c

        return multiply

    return comp_addition


# addition_int = 10
# copy_addition_int = addition_int
# print(copy_addition_int)
copy_addition = addition
copy_result = copy_addition(2,3)
# print(copy_result)

partial_result=partial_addition(2)
final_result=partial_result(3)

# print(partial_result)
print(final_result)

a =partial_addition(1)
b =a(2)
c =b(3)
print(c)

# Have a functiuon that splits a word with hypen ("Hello-Tunde") into two
# def split_text(word):
#     a = word.split('T') 
#     return a[0]
    

# word = split_text("Hello-Tunde")
# print(word)


# names =["Hello-Tunde", "Hello-Ray"...]

def split_text(word):
    a = word.split('T') 
    d = a[0] # Hello-

    def cooler_names(list_names):
        cool_names = []
        for name in list_names:
            result = d + name #Hello-Ray 
            cool_names.append(result)
        return cool_names

    return cooler_names
    

# returns a function, or accepts a function as an argument

result_function = split_text("Hello-Tunde") # fetch 10 billion databse assest from server # Hello-


names = ["Tunde", "Ray", "Jay", "Mo"]
animals = ['Dog', 'Cat', 'Pig']
automobile = ['Car', 'Bicycle', 'Tractor']

tr_names = result_function(names)
tr_animals = result_function(animals)
tr_automobile = result_function(automobile)
print(tr_names)
print(tr_animals)
print(tr_automobile)

def transform_list(word, lst):
    new_list = []
    for item in lst:
       result= word + item
       new_list.append(result)
    return new_list

tr_names_2 = transform_list("Hello-", names)
tr_animals_2 = transform_list("Hello-", animals)
tr_automobile_2 = transform_list("Hello-", automobile)


def subtract(a, b):
    return a - b # 10 -7  

def do_subtract(num, alg, fn):
    return fn(num, alg) # subtract(10, 7)

result = do_subtract(10, 7, subtract)
print(result)

#1#fn(10, 7) #subtarct(10, 7) => 3
#2#do_subtract(10, 7, subtract) => 3

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


def login(fn):
    def wrapper():
        # some.login(user)
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






# Write a higher order function that accepts a word, 
# #first, capitalizes the letters, 
# # then later lowercase the letters

def manipulate_words(word):
    # capital case word
    pass

    def capitalize(word):
        # lowercase word
        pass
    
    return capitalize


#Write a decorator function that capitalize a word
# defined word_capitalize  decorator that capitalizes a word

# @word_capitalize
# def get_word(word):
#     return word

# result = get_word("decorate")
# print(result) # DECORATE






