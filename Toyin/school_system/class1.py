#to create a class, class has to be uppercase
#a class allows us to construct object
##__ dunder method
#init means initialisation
#every method in a class has to have self as its first argument, self refers to the class we are dealing with
class User:
    def __init__(self, username, password, platform):
        self.username = username
        self.password = password
        self.platform = platform

facebook = User(username = 'user1', password = "user1_key", platform="facebook")
print(facebook)
#output is <__main__.User object at 0x7fe272c03d60>

#did same for instagram but got the same error message
instagram = User(username = 'user2', password = "user2_key", platform="instagram")
print(instagram)
#output is <__main__.User object at 0x7f888e82ff70>

class Location:
    pass
    # def __init__(self):
    #     pass
location_i = Location()
print(location_i)
#outpuut is <__main__.Location object at 0x7fb272b6b040>

print(facebook.username) # output is user1


#we can change the names of the argument
class User:
    def __init__(self, a, b, c):
        self.username = a
        self.password = b
        self.platform = c

facebook = User(a = 'user1', b = "user1_key", c="facebook")
instagram= User(a = 'user2', b = "user2_key", c="instagram")
print(facebook)
print(instagram)

class Location:
    pass
    # def __init__(self):
    #     pass
location_i = Location()
print(location_i) 
#the below is how to get the attribute access
print(facebook.username)#output is user1
print(instagram.username) #output is user2
#we got same asnwers as above

#we can directly replace the attribute
facebook.username="tunde"
print(facebook.username) #output is tunde

#setters and getter method
# set things on an object
# retrieve things from an object
#to set: self.thing = value
#to retrieve: self.thing
#we want to Get the username by a method
class User:
    def __init__(self, a, b, c):
        self.username = a
        self.password = b
        self.platform = c
    def get_username(self): 
        return self.username

facebook = User(a = 'user1', b = "user1_key", c="facebook")
instagram= User(a = 'user2', b = "user2_key", c="instagram")
result = facebook.get_username()
print(result) #output is user1

#Setter method
class User:
    def __init__(self, a, b, c):
        self.username = a
        self.password = b
        self.platform = c
    def get_username(self): 
        return self.username
    def set_username(self, name):
        self.username = name

facebook = User(a = 'user1', b = "user1_key", c="facebook")
instagram= User(a = 'user2', b = "user2_key", c="instagram")
facebook.set_username("Femi")
result = facebook.get_username()
print(result) #output is Femi


#another example of Set, adding +1
class User:
    def __init__(self, a, b, c):
        self.username = a
        self.password = b
        self.platform = c
    def get_username(self): 
        return self.username
    def set_username(self, name):
        self.username = name
    def set_no_of_login_attempts(self, total_login):
        self.total_login = total_login + 1

facebook = User(a = 'user1', b = "user1_key", c="facebook")
instagram= User(a = 'user2', b = "user2_key", c="instagram")
facebook.set_no_of_login_attempts(5)
print(facebook.total_login) #output is 6


#if we try to get before setting, it will return an error message
    def get_no_of_login_attempt(self):
        return self.total_login
print(facebook.get_no_of_login_attempt()) #output is an error message

# increment login attempt
class User:
    total_login = 0
    def __init__(self, a, b, c):
        self.username = a
        self.password = b
        self.platform = c
    def get_username(self): 
        return self.username
    def set_username(self, name):
        self.username = name
    def set_no_of_login_attempts(self):
        self.total_login +=1

facebook = User(a = 'user1', b = "user1_key", c="facebook")
instagram= User(a = 'user2', b = "user2_key", c="instagram")
print(facebook.set_no_of_login_attempts())
print(facebook.total_login) #output is 1
print(facebook.set_no_of_login_attempts())
print(facebook.total_login)#output will be 2 because it's incrementing


#examples of how things could be set
    def get_user_login_and_multiply_by_2(self, a, b):
        return self.total_login * b

    def set_username(self, name):
        self.username = name-#setting an attribute

    def set_no_of_login_attempts(self):
        if self.is_user_logged_():
            self.total_login +=1
            self.user_active = "Online"
            self_user_location = "London"
        return self.total_login

    def set_no_of_login_attempts(self):
        if self.is_user_logged_():
            self.total_login +=1
        return self.total_login

#Done *****************************







