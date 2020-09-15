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
    def update(self,):
        pass
    @abstractmethod
    def delete(self):
        pass
    
    

class Table(BaseTable):

    records = {}
    def get_records(self):
        return self.records

    def load_record(self):
        raise NotImplementedError

    def backup_record(self):
        raise NotImplementedError

    def get_total_records(self):
        raise NotImplementedError

    def get_average(self):
        raise NotImplementedError
   
    

        
class Student(Table):
    total = 0

    def __get_student(self,student_no):
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

    def __update_student(self,student_no, **kwargs):
        student = self.__get_student(student_no)
        if "new_gpa" in kwargs:
            student["gpa"] = kwargs["new_gpa"]
        if "new_full_name" in kwargs:
            student["full_name"] = kwargs["new_full_name"]
        return student

    def __delete_student(self,student_no):
        if student_no in self.records:
            del self.records[student_no]
        else:
            return "Sorry, it appears that student does not exist in this records."
        return self.records

    def get_file_path(self, filename):
        return os.path.join(sys.path[0], filename)


    def dump_table_to_csv(self, output_file):
        path = self.get_file_path(output_file)
        with open(path, "w", newline="") as f:
            fieldnames = ["student_no", "gpa", "full_names"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for key in self.records.values():
                writer.writerow(key)

    def load_csv_to_table(self,source_file):
        path = self.get_file_path(source_file)
        with open(path, mode="r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for row in reader:
                self.add_student(**row)
        return self.records

    def aggregate(self):
        """ returns the sum of all student gpa in student records"""
        """ returns the sum of all student gpa in student records"""
        total = 0
        list_of_gpa= ({key:values['gpa'] for key,values in self.records.items()})
        total = sum(list_of_gpa)
        return round(total,2)

    def average_gpa(self):
        """ calculete the aerage of all student gpa """
        gpa_total= self.aggregate()
        extracted_gpa= ({key:values['gpa'] for key,values in self.records.items()})
        return gpa_total/len(extracted_gpa)

class StudentTable(Student):

    def create(self, **kwargs):
        return self.add_student(**kwargs)

    def retrieve(self, student_no):
        return self.__get_student(student_no)

    def update(self,student_no,**kwargs):
        return self.__update_student(student_no, **kwargs)

    def delete(self, student_no):
        return self.__delete_student(student_no)

    def load_record(self, source_file):
        return self.load_csv_to_table(source_file)

    def backup_record(self, output_file):
        return self.dump_table_to_csv(output_file)
    
    def get_total_records(self):
        return self.aggregate()

    def get_average(self):
        return self.average_gpa()





table = StudentTable()


# result = table.create(student_no=1011, gpa=4.2, full_name="James")
# print(result)
# result = table.retrieve(1011)
# print(result)
# result = table.update(1011, new_gpa=5.0, full_name="James")
# print(result)
# result = table.delete(1011)
# print(result)
# result = table.delete(1011)
# print(result)
load = table.load_csv_to_table("student.csv")
# # print(load)
print(table.records)
sum_total= table.get_total_records()
print(sum_total)

average = table.get_average()
print(average)
# dump = table.backup_record("student_output.csv")

### Remaining 4 methods:
#Can we reclocate any of them to the Student class?
#Can we reclocate any of them to the Table class?
#Can we reclocate any of them to the StudentTable class?
#Can we create a new class for any of the methods if they don't intuiitively belong in any of the above classes.
#Do we think that all of the methods / attributes that are currently public, really need to be public methods? 
#If not, which ones need to become private? (table.get_student())
# Do we think that all of these classes should be in a single file or they need to be seperated? 
        


    


