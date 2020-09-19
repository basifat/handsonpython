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


# class Table(BaseTable):

#     records = {}

#     def get_records(self):
#         return self.records

#     def delete_record(self,entity_id):
#         if entity_id in self.records:
#             del self.records[entity_id]
#         else:
#             return "Sorry, it appears that record does not exist."
#         return self.records

#     def get_record(self,entity_id):
#         try:
#             return self.records[entity_id]
#         except KeyError:
#             return "No record matching that entity id in the table"

#     def convert_record_info_to_dict(self, **kwargs):
#         return dict(**kwargs)
    
#     def add_record(self, **kwargs):
#         row = self.convert_record_info_to_dict(**kwargs)
#         entity_id= row["entity_id"]
#         self.records[int(entity_id)] = row
#         return self.records


# class DataHandler(Table):

#     def write_record_to_csv(self, fieldnames, table_name):
#         path = self.get_file_path(table_name)
#         with open(path, "w", newline="") as f:
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             writer.writeheader()
#             for key in self.records.values():
#                 writer.writerow(key)
#         print(f"Wrote {len(self.records)} records to file." )

#     def load_records_to_table(self, table_name):
#         path = self.get_file_path(table_name)
#         with open(path, mode="r") as csv_file:
#             reader = csv.DictReader(csv_file, delimiter=",")
#             for row in reader:
#                 self.add_record(**row)
#         return self.records
    
    
#     def read_from_csv(self):
#         raise NotImplementedError

#     def write_to_csv(self):
#         raise NotImplementedError

#     def get_file_path(self, filename):
#         return os.path.join(sys.path[0], filename)


# class Student(DataHandler):
    
#     table_name = "student.csv"
#     fieldnames = ["student_no", "gpa", "full_name"]

#     def add_student(self, **kwargs):
#         return self.add_record(**kwargs)
        
         
#     def write_student_to_csv(self):
#         self.write_record_to_csv(self.fieldnames, self.table_name)

#     def read_student_records_from_csv(self):
#         return self.load_records_to_table(self.table_name)

#     def update_student(self,student_no, **kwargs):
#         student = self.get_record(student_no)
#         if "new_gpa" in kwargs:
#             student["gpa"] = kwargs["new_gpa"]
#         if "new_full_name" in kwargs:
#             student["full_name"] = kwargs["new_full_name"]
#         return student

   
# class Lecturer(DataHandler):
    
#     def add_lecturer(self, **kwargs):
#         return self.add_record(**kwargs)
        

#     def update_lecturer(self, entity_id,**kwargs):
#         lecturer_info = self.records[entity_id]
#         if "updated_courses" in kwargs:
#             lecturer_info["no_of_courses"] = kwargs["updated_courses"]

#         if "updated_no_student" in kwargs:
#             lecturer_info['no_of_student'] = kwargs["updated_no_student"]
#         return lecturer_info

    
# class LecturerTable(Lecturer):


#     def create(self, **kwargs):
#         return self.add_lecturer(**kwargs)

#     def retrieve(self, lecturer_no):
#         return self.get_record(lecturer_no)

#     def update(self,lecturer_no,**kwargs):
#         return self.update_lecturer(lecturer_no, **kwargs)

#     def delete(self, lecturer_no):
#         return self.delete_record(lecturer_no)

#     # def read_from_csv(self):
#     #     return self.load_records_to_table


# class StudentTable(Student):

#     def create(self, **kwargs):
#         return self.add_student(**kwargs)

#     def retrieve(self, student_no):
#         return self.get_record(student_no)

#     def update(self,student_no,**kwargs):
#         return self.update_student(student_no, **kwargs)

#     def delete(self, student_no):
#        return self.delete_record(student_no)

#     def write_to_csv(self):
#         self.write_student_to_csv()

#     def read_from_csv(self):
#         return self.read_student_records_from_csv()

    


# # table = LecturerTable()
# # result=table.add_lecturer(entity_id=1, full_name="John Bosco", faculty="Business IT", no_of_courses= 2, no_of_student=10, title="Egineer")
# # result=table.delete(1)
# # print(result)

# table2=StudentTable()
# reult=table2.read_from_csv()
# print(result)
#result=table.update("John Bosco", updated_no_student=20)

# result1 = table.delete("John Bosco")
# print(table.records)







