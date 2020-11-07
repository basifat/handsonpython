def get_user_login_and_multiply_by_2(a, b):
    return a * b



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

    # def set_no_of_login_attempts(self, total_login):
    #     self.total_login = total_login + 1

    def set_no_of_login_attempts(self):

        if self.is_user_logged_in():
            self.total_login +=1 
        return self.total_login
    
    def get_user_login_and_multiply_by_2(self, a, b):
        return self.total_login * b





    # set things on an object
    # retrieve things from an object
    
    #thing = 10
    #print(thing)
    # self.thing = 10
    # print(self.thing)
    # self.thing



facebook = User(a = 'user1', b = "user1_key", c="facebook")
# print(instagram)
# print(locatioh_i)
# print(facebook.username)
# print(instagram.username)
# facebook.username="tunde"
# twitter = User(username, password, platform)
print(facebook.username)
result = facebook.get_username()
print(result)

facebook.set_username("Femi")
result = facebook.get_username()
print(result)


# facebook.set_no_of_login_attempts(5)

print(facebook.set_no_of_login_attempts())
print(facebook.total_login)

print(facebook.set_no_of_login_attempts())
print(facebook.total_login)

