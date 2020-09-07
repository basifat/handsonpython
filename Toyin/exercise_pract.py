# items = [1,1,1,2,2,2,3,4,5,5]
# def unique_items():
#     unique = []
#     for item in items:
#         if item not in unique:
#             unique.append(item) #Now we use predefined function 
#     return unique
# a = unique_items()
# print(a) #Print the result





# T = ['school']
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def capwords():
    return 'manchester'

print(capwords())


