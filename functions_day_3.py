#Write a function that accepts two arguments a and b, then adds both together
def addition(a,b):
    return a+b
result=addition(2,3)
# print(result)

def partial_addition(a):

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

names = ["Tunde", "Ray", "Jay", "Mo"]
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
coolio = result_function(names)
print(coolio)


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









