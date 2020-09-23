class Garrage():
    """ this class adds car to garrage 
    and retuns the number of cars in garrage using len method"""
    
    def __init__(self):
        self.cars= []
    
    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]
    
    def __str__(self):
        return f'Garrage has {len(self.cars)} cars'


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
    """ 
    Log writes to a file using context manager. 
    Example usage :
        with Log(r"myfile.txt") as logfile: 
            logfile.logging("This is a test file, use at your own risk")
    """ 
    
    def __init__(self,filename):
        self.filename=filename
        self.fp=None    
    
    def logging(self,text):
        self.fp.write(text+'\n')
       
    def __enter__(self):
        self.fp=open(self.filename,"w+")
        return self   
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


    