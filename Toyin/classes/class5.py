from abc import ABC, abstractmethod

class GenericUniversityWallet(ABC):
    balance = 0


    def __init__(self, student_name, wallet_no, grade = None):
        self.wallet_no = wallet_no
        self.student_name = student_name
        self.grade = grade
#we can add a keyword argument grade=None into the def and it won't give any error
# # def __init__(self, student_name, wallet_no, grade = None):     

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

def rectangle(length, breadth):#was created, copied and pasted under the staticmethod in the sub class
    return length * breadth

class UniArcadaWallet(GenericUniversityWallet):
#because we are inheriting a class with an abstract method, 
#we will have to declare our own stuff
    
    
    def deposit(self, amount):
        print(amount)

    def withdraw(self, amount):
        print(amount)
        
#defining a class method: they do something to the class
    @classmethod
    def transfer(cls):
        print("This is a class method")


    @classmethod #main purpose of a class method is when u want to contruct your object in a different way
    def david_wallet(cls):
        return cls("David", 450, 80)

    # @classmethod #main purpose of a class method is when u want to contruct your object in a different way
    # def wallet_based_on_name_alphabet(cls):
    #     #if student name starts from a-d, random number >400
    #     return cls("David", 450, 80)
    #     else:
    #     return cls("David", 98, 80)#random number < 100
    
    @staticmethod #method that are never changing, every class can access it
    #writing a real function outside of the class
    def rectangle(length, breadth):
        return length * breadth

    
       

#constructing the instance
david_wallet = UniArcadaWallet("David", 468)
print(david_wallet.student_name)#output is David
#student.name is an instance variable and the def are the instance method

james_wallet = UniArcadaWallet("James", 289)
print(james_wallet.student_name) #output is James

#after adding the class method on line 30 we now want to call them
UniArcadaWallet.transfer()#output is This is a class method

new_david_wallet = UniArcadaWallet.david_wallet()
print(new_david_wallet)#output is main__.UniArcadaWallet object at 0x7feec526b400>
#this has now changed the details for David in line 41
print(new_david_wallet.grade)#output is 80

#notes:line 45 -50 is easier to declare instead of this below
#list_of_names = ["David", "James"]
#if name starts with between acor :
#wallet_no = random between 0-99
#UniArcadaWallet(name, wallet_no)
#else


#Declaring another class
class UniJosWallet(GenericUniversityWallet):
    
    def __call__(self, room_no):
        return room_no
        
    def deposit(self, amount):
        print(amount)

    def withdraw(self, amount):
        print(amount)

    def list_faculties(self):
        return ["Maths", "Medicine"]

joe_wallet = UniJosWallet("Joe", 342)#instance of unijoswallet-> joe_wallet
invoked_instance = joe_wallet(10)#invoking joewallet and passing an argument
print(invoked_instance)#output is 10



#hiding stuff : another class
class Faculties:
    def list_faculties(self):
        return ["Agric", "Pharmacy"]
    
class UniIbadanWallet(UniJosWallet, Faculties):#method resolution object(mro), u can inherit multiple class. 
#order of preference is left to right
    pass

uni_ibadan = UniIbadanWallet("Femi", 90)
faculty = uni_ibadan.list_faculties()
print(faculty) #output is ['Maths', 'Medicine']

# #but when line 111 was switched round, it printed 
# class UniIbadanWallet(Faculties, UniJosWallet):
#     pass
# faculty = uni_ibadan.list_faculties()
# print(faculty) #output is ['Agric', 'Pharmacy']

#can decide to include a method for list faculties in UniIbadanWallet
class UniIbadanWallet(Faculties, UniJosWallet):
    def list_faculties(self):
        return ["Social Science", "Law"]


uni_ibadan = UniIbadanWallet("Femi", 90)
faculty = uni_ibadan.list_faculties()
print(faculty) #output is ['Social Science', 'Law'] because its own class takes precedence

print(dir(uni_ibadan))#will list thing available if the object inherited any

#private and public**********************

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



class UniIbadanWallet(Faculties,UniJosWallet):
    def get_deen(self):
        return self.deen()

uni_ibadan=UniIbadanWallet("Femi", 90)
faculty =uni_ibadan.list_faculties()
print(faculty) #output is ['Agric', 'Pharmacy', 'Mr Banjo']

deen_name=uni_ibadan.public_deen()
print(deen_name)#output is Mr Banjo

#if we add this private into line 141 
# __deen_age =90
#deen_age = __deen_age
#then print
uni_ibadan=UniIbadanWallet("Femi", 90)
faculty =uni_ibadan.list_faculties()
print(faculty)
print(dir(uni_ibadan))
deen_name=uni_ibadan.public_deen()
print(deen_name)


#SUPER FACULTIES******************************
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
        return super().get_deen()
        

# #could decide to assign 'super' in line 204 to a variable instead then call the variable
# class UniIbadanWallet(Faculties,UniJosWallet):
#     def get_deen(self):
#         name = super().get_deen()
#         return "phd" + name
#         #output was phdMr Banjo Ojamila

#could also decide to do stuff before calling 'super' or after we call 'suoer. 
#the below is an example of before calling 'super'
#class UniIbadanWallet(Faculties,UniJosWallet):
    #def get_deen(self):
        # get all dean anmes
        # find oldest dean
        # self.oldest_dean = name 
        #return super().get_dean()

uni_ibadan=UniIbadanWallet("Femi", 90)
faculty =uni_ibadan.list_faculties()
print(faculty)
#print(dir(uni_ibadan))
deen_name=uni_ibadan.get_deen()
print(deen_name)#output is Mr Banjo Ojamila

