class Restaurant:

    def __init__(self,resturant_name, cuisine_type):
        self.name =resturant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        return self.name, self.cuisine

    
    def open_resturant(self, message):
        self.greetings = message
        print(self.greetings)
        return self.greetings

   # python inbuilt method to return string text in readble format
    def __repr__(self): 
        return f'<Restaurant name: {self.name}, cuisine type is: {self.cuisine} >'

class User:
    def __init__(self, greatings, firstname, lastname, dateofbirth, mailAdress ):
        self.name = firstname
        self.surname =lastname
        self.age =dateofbirth
        self.greet = greatings
        self.email = mailAdress
    
    def describe_user(self):
        return f"<{self.name} {self.surname} {self.age} {self.email}>"

    def greet_user(self):
        return f"< {self.greet} {self.name} {self.surname} your date of birth is {self.age} >"

# first instance of Restuarant class   
new_restuarant = Restaurant("Mama Put", "African Cuisine")
restaurant_name = new_restuarant.name
print(restaurant_name)
cuisine_type=new_restuarant.cuisine
print(cuisine_type)
restaurant_type = new_restuarant.describe_restaurant()
new_restuarant.open_resturant("we are open ")
print(restaurant_type)

# Three instances for Restaurant class
tai_buffet = Restaurant("Tai Delicacy", "Tai Cuisine")
restaurant_type1 = tai_buffet.describe_restaurant()
print(restaurant_type1)

mexican_food = Restaurant("Taco-Bell", "Mexican Cuisine")
restaurant_type2= mexican_food.describe_restaurant()
print(restaurant_type2)

indian_food =Restaurant("Deli Special", "Indian Cuisine")
restaurant_type3 = indian_food.describe_restaurant()
print(restaurant_type3)

# instances for user class
new_user = User("Hello", "Bob","Lasson", "26-01-1990", "bob@gmail.com")
print(new_user.describe_user())
print(new_user.greet_user())

new_user1 = User("Hello", "Mark","Robin", "01-03-1980", "mark@gmail.com")
print(new_user1.describe_user())
print(new_user1.greet_user())


