# full_name, GPA, student_no
import os, sys
import csv

class StudentTable:
    
    records={}
    table_name = "student.csv" 

    def __init__(self):
        self.load_csv_to_table(self.table_name)

    def get_records(self):
        return self.records

    def make_row(self, **kwargs):
        return dict(**kwargs)

    def add_row_to_records(self, **kwargs):
        row = self.make_row(**kwargs)
        student_info = row["student_no"]
        self.records[int(student_info)] = row
        self.dump_table_to_csv(self.table_name)
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

    def aggregate(self):
        """ returns the sum of all student gpa in student records"""
        total = 0
        for record in self.records.values():
            gpa=record["gpa"]
            total += gpa
        return round(total,2)

    def get_file_path(self, filename):
        return os.path.join(sys.path[0], filename)


    def dump_table_to_csv(self, output_file):
        path = self.get_file_path(output_file)
        with open(path, "w", newline="") as f:
            fieldnames = ["student_no", "gpa", "full_name"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for key in self.records.values():
                writer.writerow(key)

    def load_csv_to_table(self,source_file):
        path = self.get_file_path(source_file)
        with open(path, mode="r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for row in reader:
                self.add_row_to_records(**row)
        return self.records


table = StudentTable()
result = table.add_row_to_records(student_no=1011, gpa=4.2, full_name="James")
result = table.add_row_to_records(student_no=1012, gpa=4.2, full_name="John")
table.add_row_to_records(student_no=1013, gpa=4.2, full_name="Temi")
print(table.get_records())





# def dump_single_record(self, output_file, record):
#     path = self.get_file_path(output_file)
#     with open(path, "a", newline="\n") as f:
#         fieldnames = ["student_no", "gpa", "full_name"]
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writerow(record)
#Assignment
# Define a class for Table which will have certain abtsract methods and also certain concrete methods
# Define a class for student, which will have all the methods or attributes that students need to deal with
# Define StudentTable class for example that extends the abstract Table class, and then also extends the Student class
# 

# table_2 = StudentTable()
# print(table_2.get_records())


# table.add_row_to_records(student_no=1001, gpa=4.4, full_name="Talle")
# print(result)
# new_result= table.get_student(1002)
# print(new_result)
# new_result_2= table.update_student(1000, new_gpa=4.9)
# print(new_result_2)

# sum_gpa=table.aggregate()
# print(sum_gpa)
# table.dump_table_to_csv("student_out_put.csv")
# records =table.load_csv_to_table("student.csv")
# print(records)
# delete= table.delete_student(1000)
# print(delete)

# delete= table.delete_student(1000)
# print(delete)


