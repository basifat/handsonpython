#day 1: Thursday 03/09/2020************start of the project till tuesday 08/09/20
# student_no  | GPA  | full name
#1000        | 4.0  |James
#1001        | 4.2  |Paul

#records = [(1000, 4.0, "James"),
#(1001, 4.2, "Paul")]
#for rows in record:
#(1000, 4.0, "James") -> row[0] or row[1]

#records = [[1000, 4.0, "James"],[1001, 4.2, "Paul"] ]
#for rows in records:
#(1000, 4.0, "James") -> row[0] or row[1]


#records = [(1000, 4.0, "James"),(1001, 4.2, "Paul"), ]
#for rows in records:
#(1000, 4.0, "James") -> row[0] or row[1]



#record = {"1000":student_no(1000, 4.0, James'), "1001":student_no(1001, 4.2, 'Paul')}
#record["1000"]


#record = {"1000": {'student_no':1000, 'GPA':4.0, 'full_name':'James'}, "1001": {'student_no':1001, 'GPA':4.2, 'full_name':'Paul'}}
#record["1000"]

def row(student_no, gpa, full_name):
    return dict(student_no = student_no, GPA = gpa, full_name = full_name)

james_details = row(1000, 4.2, "James")
#print(james_details)

#records = {"1000": {'student_no':1000, 'GPA':4.2, 'full_name':'James'}, "1001": {'student_no':1001, 'GPA':4.2, 'full_name':'Paul'}}
#record = records["1000"]
#print(record) #output is {'student_no': 1000, 'GPA': 4.2, 'full_name': 'James'}
#print(record["student_no"] == 1000)


#this didn't give what we want
def add_row_to_record(row):
    records = {}
    records["key"] = row
    return records

paul_row = row(1001, 4.2, "Paul")
james_row= row(1000, 4.2, "James")

new_row = add_row_to_record(paul_row)
print(new_row) #{'key': {'student_no': 1001, 'GPA': 4.2, 'full_name': 'Paul'}}

new_row = add_row_to_record(james_row)
print(new_row)#output is {'key': {'student_no': 1000, 'GPA': 4.2, 'full_name': 'James'}}
# #didn't give what we want


#this is what we want: taking the number out of the student info and create the row with that number itself
def row(student_no, gpa, full_name):
    return dict(student_no = student_no, GPA = gpa, full_name = full_name)
    
records = {}
def add_row_to_record(row):
    student_info = row["student_no"]
    records[student_info] = row
    return records

paul_row = row(1001, 4.5, "Paul")
james_row= row(1000, 4.2, "James")
mary_row= row(1002, 4.7, "Mary")#adding new row

paul = add_row_to_record(paul_row)
james = add_row_to_record(james_row)
mary = add_row_to_record(mary_row)#with this
print(james)
#output is {1001: {'student_no': 1001, 'GPA': 4.5, 'full_name': 'Paul'}, 1000: {'student_no': 1000, 'GPA': 4.2, 'full_name': 'James'}}

#we can add one more row by just adding line 69 and 73
#output is {1001: {'student_no': 1001, 'GPA': 4.5, 'full_name': 'Paul'}, 1000: {'student_no': 1000, 'GPA': 4.2, 'full_name': 'James'}, 1002: {'student_no': 1002, 'GPA': 4.7, 'full_name': 'Mary'}}

#for i in range(0,1000):
    #add_row_to_records(row(random(1,10), below5, "Paul"))

#Assignment
#write a function that finds a student 'get_student', given the student number as an return, then return the found row
#if no student was found matching the student number, return the message "No student matching that student no in the table"

def get_student(student_no):
    try:
        return records[student_no]
    except KeyError:
        return "No student matching that student no in the table"

#update information for a specific student record
#find the student to update
#update record for found student

def update_student(student_no,):
    student_info = get_student(student_no)
    student_info['GPA'] = 4.2
    return student_info
    #print(student_info)

#print(records)
#new_rec = get_student(1002)
#print(new_rec)
updated_student = update_student(1002)
print(updated_student)


#Tuesday 08/09/20 Class

import csv

with open('/Users/oluwatoyinomole/Documents/handsonpython/Toyin/pf_project/student_input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')  
    for row in csv_reader:
        print(row)

#ways to find files in the same path(directory) in python
import csv
import os, sys

path = os.path.join(sys.path[0], 'student_input.csv')
print(path)

#this printed the csv file. with the header and then the rows
import csv
import os, sys

path = os.path.join(sys.path[0], 'student_input.csv')
print(path)

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)

# #to convert the csv file into a dictionary
import csv
import os, sys

path = os.path.join(sys.path[0], 'student_input.csv')
print(path)

with open(path, mode = "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)


#to add to record
import csv
import os, sys

path = os.path.join(sys.path[0], 'student_input.csv')
print(path)

paul_row = row(1001, 4.5, "Paul")

paul = add_row_to_record(paul_row)

with open(path, mode = "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        add_row_to_record(row)
print(records)


#just to know
#‘w’ – writing to a file
#‘r+’ or ‘w+’ – read and write to a file
#‘a’ – appending to an already existing file
#‘a+’ – append to a file after reading





