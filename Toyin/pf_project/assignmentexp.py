#Saturday 05/09/20 Class: #friday(04/09/20) Assignment explained 
#update the 'update student' function so that it allows us to change the student GPA and or the student full name.
#update_student(1002, 4.5, "Mary Jones")
#update_student(1002, "Tiger Cruze")
#update_student(1002, 4.5)
#if the function can accept arbitrary number of arguments and the function then decides how to use them


#2. write a function that finds all the student with a GPA greater than a certain number
#find_student_by_gpa(4.8)
#{"1000"; {'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, 1001: {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale}}
#[{'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}]

# def function_a(a):
#     return a +1 * 10

# a_list = [20, 490, 49, 49 ,39]
# for item in a_list:
#     transform_a = function_a(item)

def row(student_no, gpa, full_name):
    return dict(student_no = student_no, GPA = gpa, full_name = full_name)
    
records = {}
def add_row_to_record(row):
    student_info = row["student_no"]
    records[student_info] = row
    return records

paul_row = row(1001, 4.5, "Paul")
james_row= row(1000, 4.2, "James")
mary_row= row(1002, 4.7, "Mary")

paul = add_row_to_record(paul_row)
james = add_row_to_record(james_row)
mary = add_row_to_record(mary_row)
print(james)

def get_student(student_no):
    try:
        return records[student_no]
    except KeyError:
        return "No student matching that student no in the table"
        
def update_student(student_no, **kwargs):
    student_info = get_student(student_no)
    student_info['GPA'] = kwargs["new_gpa"]
    student_info['full_name'] = kwargs["new_full_name"]
    return student_info
    #print(student_info)

updated_student = update_student(1002, new_gpa = 4.5, new_full_name = "Mary Jones")
print(updated_student)

#update_student(1002, "Tiger Cruze")
def update_student(student_no, **kwargs):
    student_info = get_student(student_no)
    if 'new_gpa' in kwargs:
        student_info['GPA'] = kwargs["new_gpa"]
    student_info['full_name'] = kwargs["new_full_name"]
    return student_info
    #print(student_info)
updated_student = update_student(1002, new_full_name = "Tiger Cruze")
print(updated_student)


#update_student(1002, 4.5)
def update_student(student_no, **kwargs):
    student_info = get_student(student_no)
    if 'new_gpa' in kwargs:
        student_info['GPA'] = kwargs["new_gpa"]
    if 'new_full_name' in kwargs:
        student_info['full_name'] = kwargs["new_full_name"]
    return student_info
    #print(student_info)
updated_student = update_student(1002, new_gpa = 4.5)
print(updated_student)


#updating without using **kwargs
def update_student(student_no, new_full_name = None, new_gpa = None):
    student_info = get_student(student_no)
    student_info['GPA'] = new_gpa
    student_info['full_name'] = new_full_name
    return student_info
    #print(student_info)

updated_student = update_student(1002, new_full_name = 'Tunde', new_gpa= 5.5)
print(updated_student)

#and if we only want to change one of the 
def update_student(student_no, new_full_name = None, new_gpa = None):
    student_info = get_student(student_no)
    if new_gpa is not None:
        student_info['GPA'] = new_gpa
    student_info['full_name'] = new_full_name
    return student_info
    #print(student_info)

updated_student = update_student(1002, new_full_name = 'Tunde')
print(updated_student)


#and if we only want to change one, gpa
def update_student(student_no, new_full_name = None, new_gpa = None):
    student_info = get_student(student_no)
    if new_gpa is not None:
        student_info['GPA'] = new_gpa
    if new_full_name is not None:
        student_info['full_name'] = new_full_name
    return student_info
    #print(student_info)

updated_student = update_student(1002, new_gpa = 6.2)
print(updated_student)



#Assignment
#define a function that accepts a student number and then deletes that student recor
#example records before deleting
# records = {"1000": {'student_no':1000, 'GPA': 4.9, 'full_name': 'James'},
#             "1001":{'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}
#           }
#example records after deleting student with record '1000'
#records = {
#          "1001":{'student_no':1001, 'GPA': 4.95, 'full_name':'Tale'}
#           }

#Bonus: 
#if we try to delete a student that does not exist, we should return a message saying "sorry, it appears that student does not exist in this record "