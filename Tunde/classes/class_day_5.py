from abc import ABC, abstractmethod
class GenericUniversityWallet(ABC):
    balance = 0

    def __init__(self, student_name, wallet_no, grade=None):
        self.wallet_no = wallet_no
        self.student_name = student_name
        self.grade = grade
        

    @abstractmethod
    def deposit(self, amount):
        pass
         
    @abstractmethod
    def withdraw(self, amount):
        pass

def rectangle(length, breath):
    return length * breath


class UniArcadaWallet(GenericUniversityWallet):


    
    def withdraw(self, amount):
        print(amount)
    
    def deposit(self, amount):
        print(amount)
        return rectangle(10, 50)

    @classmethod
    def transfer(cls):
        print("this is a class method")
    
    @classmethod 
    def david_wallet(cls):
        #if student name starts from a-d,random number > 400
        return cls("David", 450, 80)
        #else
        # return cls("David", 98, 80) # random number < 100
   
    @staticmethod
    def rectangle(length, breath):
        return length * breath

        



david_wallet =UniArcadaWallet("David", 468)
print(david_wallet.student_name)

james_wallet = UniArcadaWallet("James", 289)
print(james_wallet.student_name)

UniArcadaWallet.transfer()
new_david_wallet =UniArcadaWallet.david_wallet()
print(new_david_wallet.grade)

#list_of_names =["David", "James"]
#if name starts witth between a or D:
#  wallet_no = random number between 0-99
#    UniArcadaWallet(name, wallet_no)
#else
#
class UniJosWallet(GenericUniversityWallet):

    def  __call__(self,room_no):
        return room_no
    
    def withdraw(self, amount):
        print(amount)
    
    def deposit(self, amount):
        print(amount)
        return rectangle(10, 50)
    
    def list_faculties(self,):
        return ["Maths","Medcine"]

joe_wallet=UniJosWallet("Joe",342) # created instance of UniJosWallet -> joe_wallet
invoked_instance = joe_wallet(10) # invoke the instance 
print(invoked_instance)

class Faculties:

    __deen_age =90
    deen_age = __deen_age

    def __deen(self):
        return "Mr Banjo"

    def list_faculties(self,):
        name=self.__deen()
        lst = ["Agric","Pharmacy"]
        lst.append(name)
        return lst

    def public_deen(self):
        return self.__deen()

    def get_deen(self):
        return "Mr Banjo Ojamila"



class UniIbadanWallet(Faculties,UniJosWallet):
    def get_deen(self):
        # get all dean anmes
        # find oldest dean
        # self.oldest_dean = name 
        #return super().get_dean()
        name=super().get_deen()
        return "phd " + name


    # def list_faculties(self):
      
    


uni_ibadan=UniIbadanWallet("Femi", 90)
faculty =uni_ibadan.list_faculties()
print(faculty)
# print(dir(uni_ibadan))
deen_name=uni_ibadan.get_deen()
print(deen_name)

# deen_name=uni_ibadan.public_deen()
# print(deen_name)
    

#Assignment. 
# We have already done __str__, __repr__

# Now, write a class that uses each of the following dunder methods. i.e one class per dunder method. 
# Google for information or look at documentation for what those dunder methods mean and do.
# Use dunder methods __len__, __getitem__, __iter__, __next__, __enter__ and __exit__.




