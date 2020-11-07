import csv
import os, sys

# student_no | GPA | full_name
# 1000      | 4.0 |  James
# 1001      | 4.2 |  Paul
# 1002

# records = [(1000, 4.0, "James"),
# (1001, 4.2, "Paul")
# ]
# for rows in records:
# (1000, 4.0, "James")  -> row[0] or row[1]

# records = [(1000, 4.0, "James"), (1001, 4.2, "Paul"), ]
# for rows in records:
# [1000, 4.0, "James"]  -> row[0] or row[1]


# records = [....., [1000, 4.0, "James"], [1001, 4.2, "Paul"], ]
# for rows in records:
# [1000, 4.0, "James"]  -> row[0] or row[1]


# records =  {"1000": {'student_no': 1000, 'GPA': 4.2, 'full_name': 'James'}, "1001": {'student_no': 1001, 'GPA': 4.2, 'full_name': 'Paul'}}
# dico["1000"]

# records =  {"1000": Student(1000, 4.2, James'), "1001": Student(1001, 4.2, 'Paul')}
# dico["1000"]


# class Student:

#     def __init__(self, student_no, gpa, full_name):

#         pass

# sample_student = Student(1000, 4.2, 'James')

# {'student_no': 1000, 'GPA': 4.2, 'full_name': 'James'}
def row(student_no, gpa, full_name):
    return dict(student_no=student_no, GPA=gpa, full_name=full_name)


james_row = row(1000, 4.2, "James")
# print(james_details)

# records =  {"1000": {'student_no': 1000, 'GPA': 4.2, 'full_name': 'James'}, "1001": {'student_no': 1001, 'GPA': 4.2, 'full_name': 'Paul'}}
# record = records["key"]
# print(record["student_no"] == 1000)

records = {}


def add_row_to_records(row):
    student_info = row["student_no"]
    records[student_info] = row
    return records


paul_row = row(1001, 4.5, "Paul")
mary_row = row(1002, 4.7, "Mary")

paul = add_row_to_records(paul_row)
james = add_row_to_records(james_row)
mary = add_row_to_records(mary_row)
# print(james)

# for i range(0, 1000):
# add_row_to_records()

# Asisgnment
# Write a function that finds a student 'get_student', given the student number as an return, then returns the found row.
# if no student was found matching the student number, return the message "No student matching that student no in the table"

# 2. Write a function that finds all students with a GPA greater than a certain number
# find_students_by_gpa(4.8)
# {"1000": {'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, "1001": {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}}
# [{'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}]


def get_student(student_no):
    try:
        return records[student_no]
    except KeyError:
        return "No student matching that student no in the table"


# update information for a specific student record
# find the student to update
# update record for found student
# pass 'GPA' to update_student as a keyword argument
# update existing GPA To the new gpa from keyword argument


def update_student(student_no, **kwargs):
    student_info = get_student(student_no)
    print(student_info, "student info")
    if "new_gpa" in kwargs:
        student_info["GPA"] = kwargs["new_gpa"]
    if "new_full_name" in kwargs:
        student_info["full_name"] = kwargs["new_full_name"]
    return student_info


def update_student_2(student_no, new_full_name=None, new_gpa=None):
    student_info = get_student(student_no)
    if new_gpa is not None:
        student_info["GPA"] = new_gpa

    if new_full_name is not None:
        student_info["full_name"] = new_full_name
    return student_info


# Assignment
# Update the 'update_student' function so that it allows us to change either the student GPA and or the student full name.
# update_student(1002, 4.5, "Mary Jones")
# update_student(1002, "Tiger Cruze")
# update_student(1002, 4.5)
# If the function can accept arbitrary number of arguments and the function then decides how to use them


# james="hello_world", full_name="Peter", dodldo="kdododo", unlimited=")292020202"

# print(records)
# new_rec =get_student(1002)
# print(new_rec)
# updated_student = update_student(1002, new_gpa= 5.5,new_full_name="Tunde")
# print(updated_student)

# new_student =update_student(1001, new_full_name="Tiger Cruze")
# print(new_student)

# updated_gpa =update_student(1001, new_gpa=3.5)
# print(updated_gpa)

# updated_student = update_student_2(1002, new_gpa= 5.5,new_full_name="Tunde")
# print(updated_student)


# new_student =update_student_2(1001, new_full_name="Tiger Cruze")
# print(new_student)


# new_student =update_student_2(1001, new_gpa=3.5)
# print(new_student)
# dic = {'1000': {'a': 'hello', 'b': 10, 'c': 90.9}, 'b': 29, 'm': [1,2,3,4]}
# dic = {"a": 10, "b": "Tunde", "c": 40.6}
# print(dic['1000'])


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
# If we try to delete a student that does not exist, we should return a message saying "Sorry, it appears that student does not exist in this records."


# Aggregation
## Sum the GPA for all students

records = {
    "1000": {"student_no": 1000, "GPA": 4.9, "full_name": "James"},
    "1001": {"student_no": 1001, "GPA": 4.95, "full_name": "Tale"},
    "1002": {"student_no": 1002, "GPA": 2.95, "full_name": "Sale"},
}

# return 4.9 + 4.95
# records['GPA']
# print(records['1000']["GPA"])


# def aggregate(student_no):
#     total = 0
#     for gpa in records[
#         "1000"
#     ]:  # {'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}
#         # print(gpa, "gpa printed")
#         # total = total + gpa
#         pass
#     return total
def aggregate(student_records):
    """ returns the sum of all student gpa in student records"""
    total = 0
    for record in student_records.values():
        gpa=record["GPA"]
        if gpa > 3.0:
            total += gpa
    return round(total,2)

# gpa_sum = aggregate("1000")
# print(gpa_sum)

# Assignment
# Write a an aggregate function that sums the GPA of all students (sum all the GPAs)
# Bonus 1:
# Do the sum if the GPA is greater than 3.0

# Bonus 2:
# Write a function that finds the average of the GPA of all students(gpa_sum = 9.85) --> (average = 9.85 / total_no_of_students)


def aggregate_abel(student_records):
    total_gpa = sum(
        record["GPA"] for record in student_records.values() if record["GPA"] > 3.0
    )
    return round(total_gpa, 2)


# {'1002': 2.95, '1001': 4.95, '1000': 4.9}

# sum of GPA greater than 3.0
# def aggregate_t(records):
#     list_of_gpa= ({key:values['GPA'] for key,values in records.items()})
#     print( [] > 1000000 )
#     if list_of_gpa.values() > 3.0:
#         return (sum(list_of_gpa.values()))

# sum_of_gpa_greater_than3 = aggregate_t(records)
# print(sum_of_gpa_greater_than3, "toyin aggregate")


#####
#
path = os.path.join(sys.path[0], "student.csv")
# print(path)


# with open('employee_birthday.txt', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)


paul_row = row(
    1001, 4.5, "Paul"
)  # {'student_no': '1001', 'GPA': '4.5', 'full_name': 'Paul'}

# paul = add_row_to_records(paul_row)


# with open(path, mode="r") as csv_file:
#     # csv_reader = csv.reader(csv_file, delimiter=',')
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         add_row_to_records(row)

# print(records)

##Assignment 1
# Write a function,
# # that accepts a source file (i.e 'student_input.csv' ) as an argument,
# and populates the 'records' with all the student information from the source file.
# returns nothing

##Assignment 2
## Manually add two new student information to the records so that the total number of students will become 12.
# For example
# paul_row = row(1001, 4.5, "Paul")
# paul = add_row_to_records(paul_row)

# Assignment 3
# Write a function that writes all the student information in the records to a file named "student_output.csv". It should accept the output file as an argument


def load_csv_to_table(source_file):
    path = get_file_path(source_file)
    with open(path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        for row in reader:
            add_row_to_records(row)

    return records


# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
def get_file_path(filename):
    return os.path.join(sys.path[0], filename)


def dump_table_to_csv(output_file, table):
    path = get_file_path(output_file)
    with open(path, "w", newline="") as f:
        fieldnames = ["student_no", "GPA", "full_name"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for key in table.values():
            print(key)
            writer.writerow(key)
            # f.write("%s, %s\n" % (key, table[key]))


# print(records)
# path = os.path.join(sys.path[0], "student.csv")
# path_2 = os.path.join(sys.path[0], "student_output.csv")
# dump_table_to_csv(output_file=path_2, table=records)

# example_students = [
#     {"student_no": 1000, "GPA": 4.9, "full_name": "James"},
#     {"student_no": 1000, "GPA": 4.9, "full_name": "James"},
# ]

# student_to_add = {"student_no": 1000, "GPA": 4.9, "full_name": "James"}
# student_to_update = {"student_no": 1000, "GPA": 3.2, "full_name": "James"}
# student_to_delete = {"student_no": 1005, "GPA": 3.2, "full_name": "James"}


paul_row = row(1011, 4.5, "Paul")
paul = add_row_to_records(paul_row)

example_add_single_student_info = (1012, 4.5, "Paul")


def delete_student(student_no):
    if student_no in records:
        del records[student_no]
    else:
        return "Sorry, it appears that student does not exist in this records."
    return records



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
        return add_row_to_records(student_row)
    if collection_add_students is not None:
        for record in collection_add_students:
            students = add_row_to_records(record)
        return students
    if search_student_no is not None:
        return get_student(search_student_no)
    if update_student_info is not None:
        first, second, third = update_student_info
        return update_student(str(first), new_gpa=second, new_full_name=third)
    if delete_student_info is not None:
        return delete_student(delete_student_info)
    if table_output_file is not None:
        return dump_table_to_csv(table_output_file,records)
    if table_input_file is not None:
        return load_csv_to_table(table_input_file)
    if student_no_to_aggregate is not None:
        return aggregate(student_no_to_aggregate)
    


example_students = {
   "1000": {"student_no": 1000, "GPA": 4.9, "full_name": "James"},
  "1001":  {"student_no": 1001, "GPA": 4.9, "full_name": "paul"},
}
print(records)
example_add_single_student_info =  (1001, 4.5, "Paul") # ('1002': {"new_gpa": 4.5, "new_full_name":"Paul"})
found = table(student_no_to_aggregate=example_students)
print(found)

### 
## Group functions that have similar behaviour into own files.
## create as many files as you need
## import functionalities from those files into this file for usage
