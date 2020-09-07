# Assignment from saturday class_day_5.py
# We have already done __str__, __repr__

# Now, write a class that uses each of the following dunder methods. i.e one class per dunder method. 
# Google for information or look at documentation for what those dunder methods mean and do.
# Use dunder methods __len__, __getitem__, __iter__, __next__, __enter__ and __exit__.

class H:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.fp = open(self.name)
        return self.fp

    def __exit__(self, exc, exc_value, traceback):
        print(f'Exception: {exc_value}')
        self.fp.close()

h = H('test.txt')
print(h)



#__len__ is to get the length
class Numbers:

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    
a = Numbers([22, 23, 36, 45])
#the __len__
print('length of the object =',len(a)) 
#print(a[0])

#the __getitem__
#is basically used for accessing list items, dictionary entries, array elements. for getting values
class ListOfNumbers(object):
    def __init__(self, elements=0):
        self.my_custom_list = [0] * elements

    def __setitem__(self, index, value):
        self.my_custom_list[index] = value
            
    def __getitem__(self, index):
        return "Hey you are accessing element whose value is: {}".format(index, self.my_custom_list[index])

    def __str__(self):
        return str(self.my_custom_list)

obj = ListOfNumbers(12)
obj[0] = 1
print(obj[0])
print(obj)


#__iter and __next__
class ReturnOddNumbers:

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

# create an object
a = iter(ReturnOddNumbers())

# Using next to get to the next iterator element
print(next(a))
print(next(a))
print(next(a))