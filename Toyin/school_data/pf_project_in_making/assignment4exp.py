#Tuesday Class 15/09/20-------solving the assignment from monday 14/09/20

### Remaining 4 methods:
#Can we reclocate any of them to the Student class?
#Can we reclocate any of them to the Table class?
#Can we reclocate any of them to the StudentTable class?
#Can we create a new class for any of the methods if they don't intuiitively belong in any of the above classes.
#Do we think that all of the methods / attributes that are currently public, really need to be public methods? 
#If not, which ones need to become private? (table.get_student())
# Do we think that all of these classes should be in a single file or they need to be seperated? 

# # Table abtsraction
# CRUD -> Create (add), Retrieve (get), Update, Delete
from abc import ABC, abstractmethod
import os, sys
import csv


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


class DataHandler(Table):


    def read_from_csv(self):
        raise NotImplementedError

    def write_to_csv(self):
        raise NotImplementedError

    def get_file_path(self, filename):
        return os.path.join(sys.path[0], filename)


class Student(DataHandler):
    
    table_name = "student.csv"
    fieldnames = ["student_no", "gpa", "full_name"]
    
    def write_student_to_csv(self): #took the argument 'output_file' out 
        path = self.get_file_path(self.table_name)#changed 'output_file' to self.tablename
        with open(path, "w", newline="") as f:

            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for key in self.records.values():
                writer.writerow(key)
        print(f"Wrote {len(self.records)} records to file." )

    def load_student_records_to_table(self):#took out the argument'source_file'
        path = self.get_file_path(self.table_name)#changes the argument 'source_file\ to 'self.table_name'
        with open(path, mode="r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for row in reader:
                self.add_student(**row)
        return self.records

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
        # find a way to write each student to table, incrementally
        self.write_student_to_csv()#'self.tablename' was removed
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

    def write_to_csv(self): #took out the argument 'output_file' 
        self.write_student_to_csv()#took out the argument 'output_file'

    def read_from_csv(self):#took out the argument 'source_file'
        return self.load_student_records_to_table()#removed the argument 'source_file'



#Assignment
#Create a class Lecturer
# full_name, faculty, no_of_courses, no_of_students, title

#Add a lecturer
#Update a lecturer info
#delete a lecturer info
#get a lecturer info


        
table = StudentTable()
# result = table.create(student_no=1011, gpa=4.2, full_name="James")
# print(result)
# result = table.retrieve(1011)
# print(result)
# result = table.update(1011, new_gpa=5.0, full_name="James")
# print(result)
# esult = table.delete(1011)
# print(rersult)
# result = table.delete(1011)
# print(result)
# table.write_to_csv()
result = table.read_from_csv()#removed 'student.csv' as an argument
print(result)
result = table.load_student_records_to_table()#removed 'student.csv' as an argument
print(result)