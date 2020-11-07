#assignment 1
#write a function
#that accepts a source file(i.e student_input.csv') as an argument
#and populates the records with all the student information from the source file
#return nothing

#manually add two new student information to the records so that the total number of students will become 12
#for example
# paul_row = row(1001, 4.5, "Paul")
#paul = add_row_to_records(paul_row)

#assignment 2
#write a function that writes all the student information in the records to a file names "student_output.csv".
#it should accept the output file as an argument
#write_to_file("student_output_csv")

import csv
import os, sys

def row(student_no, gpa, full_name):
    return dict(student_no = student_no, GPA = gpa, full_name = full_name)
    
records = {}
def add_row_to_record(row):
    student_info = row["student_no"]
    records[student_info] = row
    return records

path = os.path.join(sys.path[0], 'student_input.csv')

def get_next(path):
    with open(path, mode = "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            a = add_row_to_record(row)
        return a
        
ces = get_next(path)
print(ces)


#manually add two new student information to the records 

paul_row = row(1001, 4.5, "Paul")
james_row= row(1000, 4.2, "James")

paul = add_row_to_record(paul_row)
james = add_row_to_record(james_row)
print(records)


#write a function that writes all the student information in the roecords to a file names "student_output.csv".
#it should accept the output file as an argument
#write_to_file("student_output.csv")


with open("student_output.csv", "w") as f:
    writer = csv.writer(f)
    for i in records:
      writer.writerow([i, records[i]])
f.close()



