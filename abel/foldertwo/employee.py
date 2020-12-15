from datetime import date 

class Employee:
    """ 
    The Employee Class defines age and name of employee 
    and also method to determine if employee age is a legal age.
    
    """
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.age_group = []

    @staticmethod
    def get_legal_age(ages):
        age_group = []
        legal_age = 18
        for age in ages:
            if age >= legal_age:
              age_group.append(age)
            else:
                return "no legal age found" 
        return age_group
        
                
    @classmethod
    def get_employee_age(cls, name, year):
        return cls(name, date.today().year - year)

    def __str__(self):
        return f"{self.name} is {self.age} years old "


