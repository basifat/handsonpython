# Table abtsraction
# CRUD -> Create (add), Retrieve (get), Update, Delete
from abc import ABC, abstractmethod

class BaseTable(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def retrieve(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass


class Table(BaseTable):

    records = {}

    def get_records(self):
        return self.records


class Student(Table):
    

    def get_student(self,student_no):
        try:
            return self.records[student_no]
        except KeyError:
            return "No student matching that student no in the table"
    
    def convert_student_info_to_dict(self, **kwargs):
        return dict(**kwargs)


    def add_student(self, **kwargs):
        row = self.convert_student_info_to_dict(**kwargs)
        student_info = row["student_no"]
        self.records[int(student_info)] = row
        #self.dump_table_to_csv(self.table_name)
        return self.records

    def update_student(self,student_no, **kwargs):
        student = self.get_student(student_no)
        if "new_gpa" in kwargs:
            student["gpa"] = kwargs["new_gpa"]
        if "new_full_name" in kwargs:
            student["full_name"] = kwargs["new_full_name"]
        return student

    def delete_student(self,student_no):
        if student_no in self.records:
            del self.records[student_no]
        else:
            return "Sorry, it appears that student does not exist in this records."
        return self.records


class StudentTable(Student):

    def create(self, **kwargs):
        return self.add_student(**kwargs)

    def retrieve(self, student_no):
        return self.get_student(student_no)

    def update(self,student_no,**kwargs):
        return self.update_student(student_no, **kwargs)

    def delete(self, student_no):
        return self.delete_student(student_no)


### Remaining 4 methods:
#Can we reclocate any of them to the Student class?
#Can we reclocate any of them to the Table class?
#Can we reclocate any of them to the StudentTable class?
#Can we create a new class for any of the methods if they don't intuiitively belong in any of the above classes.
#Do we think that all of the methods / attributes that are currently public, really need to be public methods? 
#If not, which ones need to become private? (table.get_student())
# Do we think that all of these classes should be in a single file or they need to be seperated? 

        

table = StudentTable()
result = table.create(student_no=1011, gpa=4.2, full_name="James")
print(result)
result = table.retrieve(1011)
print(result)
result = table.update(1011, new_gpa=5.0, full_name="James")
print(result)
result = table.delete(1011)
print(result)
result = table.delete(1011)
print(result)







    


    



    



