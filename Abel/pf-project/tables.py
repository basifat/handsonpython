import csv
import os
import sys

# student_no| GPA  | full_names
# 1000      | 4.9  | james
# 1001      | 3.5  | paul

# record = {"1000":{"student_no": 1000, "GPA": 4.9, "full_names": "james"}, "1001":{"student_no": 1001, "GPA": 3.5, "full_names": "paul"} }


def row(student_no, gpa, full_names):
    """ this function creates a dictionary record """
    return dict(student_no=student_no, GPA=gpa, full_names=full_names)


record = {}


def add_row_to_record(row):
    student_info = row["student_no"]
    record[student_info] = row
    return record

# write a function that finds a student(get_student), given the student no as argument and returns row
# if no student was found matching the student number, return the message no student no matching that number on the table


def get_student(student_no):
    """ this function takes in student no and returns found student details"""
    try:
        return record[student_no]
    except KeyError:
        return "no student no matching that number on the table"

# Assignment : update the 'update_student' functions so that it allows us to change either or both of the student GPA or fullnames
# update student (1000, 1.5, Tiger Cruz)
# update student (1001, Roger miller)
# update student(1000, 8.5)

def aggregate_2(student_records):
    """ returns the sum of all student gpa in student records"""
    total = 0
    for record in student_records.values():
        gpa=record["GPA"]
        if gpa > 3.0:
            total += gpa
    return round(total,2)

def average_gpa_2(student_records):
    """ calculete the aerage of all student gpa """
    gpa_total= aggregate_2(student_records)
    extracted_gpa = [record['GPA'] for record in student_records.values() if record["GPA"] > 3]
    return gpa_total/len(extracted_gpa)

def update_student(student_no, **kwargs):
    student_info = record[student_no]
    # print(kwargs)
    if "new_gpa" in kwargs:
        student_info["GPA"] = kwargs["new_gpa"]

    if "new_full_names" in kwargs:
        student_info['full_names'] = kwargs["new_full_names"]
    return student_info


def update_student_record(student_no, new_full_names=None, new_gpa=None):
    student_info = record[student_no]
    if "new_full_names" != None:
        student_info["full_names"] = new_full_names
    if "new_gpa" != None:
        student_info["GPA"] = new_gpa
    return student_info


# defining student details
james_row = {"student_no": 1000, "GPA": 4.9, "full_names": "james"}
paul_row = {"student_no": 1001, "GPA": 3.9, "full_names": "paul"}

# adding student row to record
# james_key = add_row_to_record(james_row)

# paul_key = add_row_to_record(paul_row)

# new_update= update_student_record(1001, new_gpa=6.0, new_full_names="Don Raymond")


# # updating student details
# updated= update_student(1000, new_gpa =1.5,new_full_names="Tiger Cruz")
# print(updated)
# updated_name = update_student(1001, new_full_names= "Roger Miller")
# print(updated_name)
# updated_gpa = update_student(1000, new_gpa= 8.5)
# print(updated_gpa)


# Assignment

# define a function that accepts a student no and then deletes that student record

# example records before deleting
# records = {
#               "1000": {'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'},
#               "1001": {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}
#           }

# example records after deleting student with record '1000'
# records = {
#               "1001": {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}
#           }

# Bonus:
# If we try to delete a student that does not exist, we should return a message saying
# "Sorry, it appears that student does not exist in this records."

# Task one: find the student
# Task two: delete the student

def delete_student(student_no):
    if student_no in record:
        del record[student_no]
    else:
        return "Sorry, it appears that student does not exist in this records."
    return record

def get_file_path(filename):
    return os.path.join(sys.path[0], filename)
# delete student with id 1000
# delete =delete_student(1000)
# print(delete)

# records = {
#               "1000": {'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'},
#               "1001": {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'},
#               "1002": {'student_no': 1001, 'GPA': 2.9, 'full_name': 'Peter'}
#           }


# with open(file_path) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for row in csv_reader:
#         print(row)

# with open(file_path,mode="r") as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter=",")
#     for row in csv_reader:
#         print(add_row_to_record(row))

# Assignment 1: write a function that accept a source_file as an argument and populate
# the 'record ' with all the student info from the source file.
# Assignment 2: write a function that writes all info of student in the 'record' to a new file named "student_output.csv"
# task: open the


def load_csv_to_table(source_file):
    get_file_path(source_file)
    with open(source_file,mode="r") as csv_file:
        reader = csv.DictReader(csv_file,delimiter=",")
        for row in reader:
            add_row_to_record(row)


# print(record)

# with open('names.csv', 'w', newline='') as csvfile:
    # fieldnames = ['first_name', 'last_name']
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # writer.writeheader()
    # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})

def dump_table_to_csv(output_file, table):
    get_file_path(output_file)
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['student_no', 'GPA', 'full_names']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key in table.values():
            writer.writerow(key)

susan = row("1011", 4.8, "Susan jones")
susan_row = add_row_to_record(susan)
andrew = row("1012", 1.1, "Andrew, Peters")
andrew_row = add_row_to_record(andrew)

input_file = os.path.join(sys.path[0], "student.csv")
outputfile = os.path.join(sys.path[0], "student_output.csv")

# load_csv_to_table(input_file)
# print(record)
#dump_table_to_csv(outputfile, record)
# print(record)


def table(
    search_student_no=None,
    add_single_student=None,
    collection_add_students=None,
    update_student_info=None,
    delete_student_info=None,
    table_output_file=None,
    table_input_file=None,
    student_no_to_aggregate =None
):
    if add_single_student is not None:
        student_row = row(*add_single_student)
        return add_row_to_record(student_row)

    if collection_add_students is not None:
        for record in collection_add_students:
            students = add_row_to_record(record)
        return students
    if search_student_no is not None:
        return get_student(search_student_no)
    if update_student_info is not None:
        first, second, third = update_student_info
        return update_student(str(first), new_gpa=second, new_full_name=third)
    if delete_student_info is not None:
        return delete_student(delete_student_info)
    if table_output_file is not None:
        return dump_table_to_csv(table_output_file, record)
    if table_input_file is not None:
        return load_csv_to_table(table_input_file)
    if student_no_to_aggregate is not None:
        return aggregate_2(student_no_to_aggregate)


new_student_entry = {"1013", 9.0, "John Bull"}

example_students = [
    {"student_no": 1014, "GPA": 9.9, "full_name": "Linus"},
    {"student_no": 1015, "GPA": 4.9, "full_name": "Simon"},
]
print(record)
example_info_to_update =  ("1012", 4.5, "Paul")

found_student = table(update_student_info=example_info_to_update)
print(found_student)


