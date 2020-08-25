def describe_restaurant(self, name,cuisine):
        self.name = name
        self.cuisine = cuisine
        print(self.name, self.cuisine)
        return self.name, self.cuisine

    def open_resturant(self, message):
        self.greetings = message
        return self.greetings

    # python inbuilt method to return string text in readble format
    def __repr__(self): 
        return f'<Restaurant name: {self.name}, cuisine type is: {self.cuisine} >'

class User:
    def __init__(self, greatings, firstname, years, ):
        self.name = firstname
        self.age =years
        self.greet = greatings

    def __repr__(self):
       return f'< {self.greet} {self.name} you are {self.age} years old >' 
        
    
new_restuarant = Restaurant("Mama Put", "African Cuisine")
print(new_restuarant)
print(new_restuarant.open_resturant("we are open"))

user_1 = User("hello", "john", "15")
print(user_1)