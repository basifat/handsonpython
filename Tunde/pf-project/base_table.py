# Table abtsraction
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

    def delete_record(self,entity_id):
        if entity_id in self.records:
            del self.records[entity_id]
        else:
            return "Sorry, it appears that record does not exist."
        return self.records
    
    def get_record(self,entity_id):
        try:
            return self.records[entity_id]
        except KeyError:
            return "No record matching that entity id in the table"

    def convert_record_info_to_dict(self, **kwargs):
        return dict(**kwargs)



class DataHandler(Table):


    def read_from_csv(self):
        raise NotImplementedError

    def write_to_csv(self):
        raise NotImplementedError

    def get_file_path(self, filename):
        return os.path.join(sys.path[0], filename)

    def write_records_to_csv(self, fieldnames, table_name):
        path = self.get_file_path(table_name)
        with open(path, "w", newline="") as f:

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for key in self.records.values():
                writer.writerow(key)
        print(f"Wrote {len(self.records)} records to file." )


class Student(DataHandler):
    
    table_name = "student.csv"
    fieldnames = ["entity_id", "gpa", "full_name"]
    
    def write_students_to_csv(self):
        self.write_records_to_csv(self.fieldnames, self.table_name)

    def load_student_records_to_table(self):
        path = self.get_file_path(self.table_name)
        with open(path, mode="r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for row in reader:
                self.add_student(**row)
        return self.records

    def add_student(self, **kwargs):
        row = self.convert_record_info_to_dict(**kwargs)
        student_info = row["entity_id"]
        self.records[int(student_info)] = row
        # find a way to write each student to table, incrementally
        self.write_students_to_csv()
        return self.records

    def update_student(self,entity_id, **kwargs):
        student = self.get_record(entity_id)
        if "new_gpa" in kwargs:
            student["gpa"] = kwargs["new_gpa"]
        if "new_full_name" in kwargs:
            student["full_name"] = kwargs["new_full_name"]
        return student

    


class StudentTable(Student):

    def create(self, **kwargs):
        return self.add_student(**kwargs)

    def retrieve(self, student_no):
        return self.get_record(student_no)

    def update(self,student_no,**kwargs):
        return self.update_student(student_no, **kwargs)

    def delete(self, student_no):
        return self.delete_record(student_no)

    def write_to_csv(self):
        self.write_students_to_csv()

    def read_from_csv(self):
        return self.load_student_records_to_table()


class Lecturer(DataHandler):
    

    def add_lecturer(self, **kwargs):
        row = self.convert_record_info_to_dict(**kwargs)
        entity_id= row["entity_id"]
        self.records[int(entity_id)] = row
        return self.records
        
    def update_lecturer(self, entity_id,**kwargs):
        lecturer_info = self.records[entity_id]
        if "updated_courses" in kwargs:
            lecturer_info["no_of_courses"] = kwargs["updated_courses"]

        if "updated_no_student" in kwargs:
            lecturer_info['no_of_student'] = kwargs["updated_no_student"]
        return lecturer_info

  


class LecturerTable(Lecturer):


    def create(self, **kwargs):
        return self.add_lecturer(**kwargs)

    def retrieve(self, lecturer_no):
        return self.get_record(lecturer_no)

    def update(self,lecturer_no,**kwargs):
        return self.update_lecturer(lecturer_no, **kwargs)

    def delete(self, lecturer_no):
        return self.delete_record(lecturer_no)

    # def write_to_csv(self):
    #     self.write_student_to_csv()

    # def read_from_csv(self):
    #     return self.load_student_records_to_table()

table = LecturerTable()
result=table.add_lecturer(entity_id=1, full_name="John Bosco", faculty="Business IT", no_of_courses= 2, no_of_student=10, title="Egineer")
print(result)
#result=table.add_lecturer(full_name="Wole Soyinka", faculty="Law", no_of_courses= 1, no_of_student=30, title="Professor")
#result=table.update("John Bosco", updated_no_student=20)

#result1 = table.delete("John Bosco")
#print(table.records)

    


### Remaining 4 methods:
#Can we reclocate any of them to the Student class?
#Can we reclocate any of them to the Table class?
#Can we reclocate any of them to the StudentTable class?
#Can we create a new class for any of the methods if they don't intuiitively belong in any of the above classes.
#Do we think that all of the methods / attributes that are currently public, really need to be public methods? 
#If not, which ones need to become private? (table.get_student())
# Do we think that all of these classes should be in a single file or they need to be seperated? 


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
result = table.read_from_csv()
print(result)


#Assignment
# Move the 'load_student_records_to_table' method into the DataHandler class and use that for handling loading of students as well as lecturer.








    


    



    



