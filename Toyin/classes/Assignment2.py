# Assignment after class_day_1.py

#1.1 Restaurant: Make a class called Restaurant. The _init_() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

# 1.2. Three Restaurants: Start with your class from Exercise 1.1. Create three different instances from the class, 
# and call describe_restaurant() for each instance. 

#1.3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several 
# other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary 
# of the user's information. Make another method called greet_user() that prints a personalized greeting to the user. 
# Create several instances representing different users, and call both methods for each user
# assignment 1.1(a)

class Restaurant:
    def __init__(self, a, b):
        self.restaurant_name = a
        self.cuisine_type = b

    def get_describe_restaurant(self):
        return self.restaurant_name

    def get_describe_restaurant_2(self):
        return self.cuisine_type

food_place= Restaurant(a="Vermillion", b="Indian")

print(food_place.get_describe_restaurant())
print(food_place.get_describe_restaurant_2())

#without a method
print(food_place.restaurant_name)
print(food_place.cuisine_type)

# 1.1(b)
    def set_open_restaurant(self, restaurant)
        self.restaurant


#assignment 1.2
class Restaurant:
    def __init__(self, a, b, c):
        self.restaurant_name = a
        self.cuisine_type = b
        self.content = c

describe = Restaurant(a="Vermillion", b="Indian", c="spices")
print(describe.restaurant_name)
print(describe.cuisine_type)
print(describe.content)

#assignment 1.3
class User:
    def __init__(self, first_name, last_name, middle_name, maiden_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.maiden_name = maiden_name

    def __str__(self):
        return f"Customer {self.first_name} with last name {self.last_name} with middle name {self.middle_name} with maiden name {self.maiden_name}."
        
        
    #def get_describe_user(self):
    #     return self.first_name
    # def get_describe_user_2(self):
    #     return self.last_name
    # def get_describe_user_3(self):
    #     return self.middle_name
    # def get_describe_user_4(self):
    #     return self.maiden_name

names = User("Debs", "Ade", "Tosin", "oni")
print(names)




