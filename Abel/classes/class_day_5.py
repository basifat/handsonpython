from datetime import date 
class Employee:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.age_group = []

    @staticmethod
    def get_legal_age(ages):
        age_group = []
        for age in ages:
            if age >=18:
              age_group.append(age)
            else:
                print("no legal age found") 
        return age_group
        
                
    @classmethod
    def get_employee_age(cls, name, year):
        return cls(name, date.today().year - year)

    def __str__(self):
        return f"{self.name} is {self.age} years old "

age_list = [10, 15, 25, 19, 30, 40]
emp = Employee("Mark Angel", 25)

get_age = emp.get_legal_age(age_list)
print(get_age)

print(Employee.get_employee_age("Jack Robinson", 1990))

#Now, write a class that uses each of the following dunder methods. i.e one class per dunder method. 
# Google for information or look at documentation for what those dunder methods mean and do.
# Use dunder methods __len__, __getitem__, __iter__, __next__, __enter__ and __exit__.

class Garrage():

    def __init__(self):
        self.cars= []
    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]
    
    def __str__(self):
        return f'Garrage has {len(self.cars)} cars'

mercedes = Garrage()
mercedes.cars.append("A-class")
mercedes.cars.append("GLC")
print(mercedes[1])


class PowerOfTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

pow_two = iter(PowerOfTwo(10))
print(next(pow_two))
print(next(pow_two))

class Log:
    
    def __init__(self,filename):
        self.filename=filename
        self.fp=None    
    
    def logging(self,text):
        self.fp.write(text+'\n')
    
    # def __enter__(self):
    #     print("__enter__")
    #     self.fp=open(self.filename,"w+")
    #     return self    
    
    def __enter__(self):
        print("__enter__")
        self.fp=open(self.filename,"w+")
        return self   
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.fp.close()

with Log(r"myfile.txt") as logfile:
    print("Main")
    logfile.logging("This is a test file, use at your own risk")
    #logfile.logging("Test2")





