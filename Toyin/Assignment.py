# Assignment 1
# Write a higher order function that accepts a word, 
# first, capitalizes the letters, 
# then later lowercase the letters

T = ['school']
def manipulate_words(word):
    capitalize = []
    for item in word:
        item= item.upper()
        capitalize.append(item)
    return capitalize
result = manipulate_words(T)
print(result)


# then later lowercase the letters
Q = ['SCHOOL']
def manipulate_words(word):
    a = []
    for item in word:
        item= item.lower()
        a.append(item)
    return a
lowercase = manipulate_words(Q)
print(lowercase)



# Assignment 2
#write a decorator function that capitalise a word
#









    


    


