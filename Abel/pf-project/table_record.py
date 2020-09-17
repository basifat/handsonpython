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


class DataHandler(Table):


    def read_from_csv(self):
        raise NotImplementedError

    def write_to_csv(self):
        raise NotImplementedError

    def get_file_path(self, filename):
        return os.path.join(sys.path[0], filename)


class Student(DataHandler):
    
    table_name = "student.csv"
    fieldnames = ["student_no", "gpa", "full_names"]

    def convert_student_info_to_dict(self, **kwargs):
        return dict(**kwargs)


    def add_student(self, **kwargs):
        row = self.convert_student_info_to_dict(**kwargs)
        student_info = row["student_no"]
        self.records[int(student_info)] = row
        #self.dump_table_to_csv(self.table_name)
        # find a way to write each student to table, incrementally
        #self.write_student_to_csv()
        return self.records

    def write_student_to_csv(self):
        path = self.get_file_path(self.table_name)
        with open(path, "w", newline="") as f:

            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writeheader()
            for key in self.records.values():
                writer.writerow(key)
        print(f"Wrote {len(self.records)} records to file." )

    def load_student_records_to_table(self):
        path = self.get_file_path(self.table_name)
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

    
    



class Lecturer(DataHandler):
    
    def create(self, **kwargs):
        return dict(**kwargs)

    def add_lecturer(self, **kwargs):
        row = self.create(**kwargs)
        lecturer_info= row["full_name"]
        self.records[lecturer_info] = row
        return self.records
        
    def update(self, full_name,**kwargs):
        lecturer_info = self.records[full_name]
        if "updated_courses" in kwargs:
            lecturer_info["no_of_courses"] = kwargs["updated_courses"]

        if "updated_no_student" in kwargs:
            lecturer_info['no_of_student'] = kwargs["updated_no_student"]
        return lecturer_info

    def retrieve(self,full_name):
        try:
            return self.records[full_name]
        except KeyError:
            return "No lecturer matching that name in the table"


    def delete(self, full_name):
        if full_name in self.records:
            del self.records[full_name]
        else:
            return "Sorry, it appears that lecturer name does not exist in this records."
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

    def write_to_csv(self):
        self.write_student_to_csv()

    def read_from_csv(self):
        return self.load_student_records_to_table()

    


table = Lecturer()
result=table.add_lecturer(full_name="John Bosco", faculty="Business IT", no_of_courses= 2, no_of_student=10, title="Egineer")
result=table.add_lecturer(full_name="Wole Soyinka", faculty="Law", no_of_courses= 1, no_of_student=30, title="Professor")
result=table.update("John Bosco", updated_no_student=20)

result1 = table.delete("John Bosco")
print(table.records)




#Create a class Lecturer
# full_name, faculty, no_of_courses, no_of_students, title

#Add a lecturer
#Update a lecturer info
#delete a lecturer info
#get a lecturer info


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
#table.write_to_csv()
#print(table.records)


