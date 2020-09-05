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

#records =  {"1000": {'student_no': 1000, 'GPA': 4.2, 'full_name': 'James'}, "1001": {'student_no': 1001, 'GPA': 4.2, 'full_name': 'Paul'}}
#record = records["key"]
#print(record["student_no"] == 1000)

records = {}

def add_row_to_records(row):
    student_info =row["student_no"] 
    records[student_info] = row
    return records

paul_row = row(1001, 4.5, "Paul")
mary_row = row(1002, 4.7, "Mary")

paul = add_row_to_records(paul_row)
james = add_row_to_records(james_row)
mary = add_row_to_records(mary_row)
# print(james)

#for i range(0, 1000):
    #add_row_to_records()

# Asisgnment 
#Write a function that finds a student 'get_student', given the student number as an return, then returns the found row.
#if no student was found matching the student number, return the message "No student matching that student no in the table"

#2. Write a function that finds all students with a GPA greater than a certain number
# find_students_by_gpa(4.8)
# {"1000": {'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, "1001": {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}}
#[{'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}]

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

    if 'new_gpa' in kwargs:
        student_info['GPA'] = kwargs["new_gpa"]
    if "new_full_name" in kwargs:
        student_info["full_name"] = kwargs["new_full_name"]
    return student_info


def update_student_2(student_no, new_full_name = None, new_gpa = None):
    student_info = get_student(student_no)
    if new_gpa is not None:
        student_info['GPA'] = new_gpa
    
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

#print(records)
#new_rec =get_student(1002)
#print(new_rec)
# updated_student = update_student(1002, new_gpa= 5.5,new_full_name="Tunde")
# print(updated_student)

# new_student =update_student(1001, new_full_name="Tiger Cruze")
# print(new_student)

# updated_gpa =update_student(1001, new_gpa=3.5)
# print(updated_gpa)

updated_student = update_student_2(1002, new_gpa= 5.5,new_full_name="Tunde")
print(updated_student)


new_student =update_student_2(1001, new_full_name="Tiger Cruze")
print(new_student)


new_student =update_student_2(1001, new_gpa=3.5)
print(new_student)
# dic = {'1000': {'a': 'hello', 'b': 10, 'c': 90.9}, 'b': 29, 'm': [1,2,3,4]}
# dic = {"a": 10, "b": "Tunde", "c": 40.6}
# print(dic['1000'])



#Assignment

# define a function that accepts a student no and then deletes that student record

# example records before deleting
# records = {
#               "1000": {'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, 
#               "1001": {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}
#           }

#example records after deleting student with record '1000'
# records = {
#               "1001": {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}
#           }

#Bonus:
#If we try to delete a student that does not exist, we should return a message saying "Sorry, it appears that student does not exist in this records."









