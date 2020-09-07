#Assignment1 03/08/2020
#write a function that finds a student 'get_student', given the student number as an return, then return the found row
#if no student was found matching the student number, return the message "No student matching that student no in the table"

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

#update information for a specific student record
#find the student to update
#update record for found student

def update_student(student_no):
    student_info = get_student(student_no)
    student_info['GPA'] = 4.2
    student_info['full_name'] = 'Mary Jones'
    return student_info
    #print(student_info)


# def update_student(student_no):
#     student_info = get_student(student_no)
#     return (student_info['GPA'] == 4.2 or student_info['full_name'] == 'Mary Jones')
    
    #print(student_info)

#print(records)
#new_rec = get_student(1002)
#print(new_rec)
updated_student = update_student(1002)
print(updated_student)


# #Assignment
# #update the 'update student' function so that it allows us to change the student GPA and or the student full name.
# #update_student(1002, 4.5, "Mary Jones")
# #update_student(1002, "Tiger Cruze")
# #update_student(1002, 4.5)
#if the function can accept arbitrary number of arguments and the function then decides how to use them



# #2. write a function that finds all the student with a GPA greater than a certain number
# #find_student_by_gpa(4.8)
# #{"1000"; {'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, 1001: {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale}}
# #[{'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}]


# def find_student_by_gpa(row):
def row(student_no, gpa, full_name):
    return dict(student_no = student_no, GPA = gpa, full_name = full_name)
    
records = {}
def add_row_to_record(row):
    student_info = row["student_no"]
    records[student_info] = row
    return records


    # if records ['GPA'] > 4.9:
    #     return records
    # else:
    #     return 'GPA' == 0



paul_row = row(1001, 4.5, "Paul")
james_row= row(1000, 4.2, "James")
mary_row= row(1002, 4.7, "Mary")#adding new row

paul = add_row_to_record(paul_row)
james = add_row_to_record(james_row)
mary = add_row_to_record(mary_row)#with this
print(james)  

def find_student_by_gpa():


       


