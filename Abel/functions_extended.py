# write a function that returns a + b

def addition(a, b):
    return a+b

result = addition(2,3)
print(result)


def partial_addition(a):

    def complete_addition(b):
        d = a+b
        
        def multiply(c):
            return d * c
        return multiply

    return complete_addition

partial_result = partial_addition(2)
com_result =partial_result(3)
final = com_result(2)
print(final)

# write a higer order function that split a word ("Hello-Tunde") in two, adding the first index of the string 
# to other strings and return a list
# # in the function declear another function that does transfomation of names
# def spit_text(word):
# word =spit_text("hello-tunde")
# a = word.split("t")
# output = ['hello-jen', 'hello-ben', 'hello-ken', 'hello-meg']


def split_text(word):
    a = word.split("t")
    d= a[0]
    def transformed_names(name_list):
        new_names = []
        for name in name_list:
            result=d + name
            new_names.append(result)
        return new_names
    
    return transformed_names

names = ["jen","ben","ken","meg"]

cool_names = split_text("hello-tunde")
cooler_names = cool_names(names)
print(cooler_names)

# write a higher order function that accepts a word
# first capitalize the words 
# then turn the word to lowercase
# takes word e.g ball = BALL

def manipulate_word(word):
    cap_word = word.swapcase()
    
    def capitalize(word):
        word = cap_word
        return word.swapcase()
    
    return capitalize

upercase = manipulate_word("BALL")
lowercase = upercase("BALL")
print(lowercase)
