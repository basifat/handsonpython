#Assignment saturday 05/09/20
#define a function that accepts a student number and then deletes that student record
#example records before deleting
# records = {"1000": {'student_no':1000, 'GPA': 4.9, 'full_name': 'James'},
#             "1001":{'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}
#           }
#example records after deleting student with record '1000'
#records = {
#          "1001":{'student_no':1001, 'GPA': 4.95, 'full_name':'Tale'}
#           }

#Bonus: 
#if we try to delete a student that does not exist, we should return a message saying "sorry, it appears that student does not exist in this record"

def row(student_no, gpa, full_name):
    return dict(student_no = student_no, GPA = gpa, full_name = full_name)
    
records = {}
def add_row_to_record(row):
    student_info = row["student_no"]
    records[student_info] = row
    return records

james_row= row(1000, 4.9, "James")
tale_row= row(1001, 4.95, "Tale")

james = add_row_to_record(james_row)
tale = add_row_to_record(tale_row)
print(james)


# def get_student(student_no):
#     try:
#         return records[student_no]
#     except KeyError:
#         return "No student matching that student no in the table"

#i don't know what i did hear but no error*************  TRIAL
# def delete_row_to_record(student_no):
#     student_info_2 = get_student(student_no)
#     del student_info_2[1000]
#     return student_info_2


# def delete_row_to_record(student_no):
#     student_info = get_student(1000)
#     del student_info
#     print(records)
#***********************************************************TRIAL END

#to delete a record: this worked---------method 1
def delete_student_record(records, key):
    recordz = records.copy()
    recordz.pop(key)
    return recordz

student_record= {"1000": {'student_no':1000, 'GPA': 4.9, 'full_name': 'James'}, "1001":{'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}}
#key_to_remove = "1000"
new_record = delete_student_record(student_record, "1002")
print(new_record) 


#to delete:*****************method 2
def remove_a_key(records, key):
    recordz = dict(records)
    del recordz[key]
    return recordz


student_record= {"1000": {'student_no':1000, 'GPA': 4.9, 'full_name': 'James'}, "1001":{'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}}
#key = "1000"
new_record = remove_a_key(student_record, "1000")
print(new_record) 
    
   
#to delete a student that does not exist and add the comment: had to use method 2 because method one was only returning same value
def remove_a_key(records, key):
    recordz = dict(records)
    try:
        del recordz[key]
        return recordz
    except KeyError:
        return "Sorry, it appears that student does not exist in this record"

student_record= {"1000": {'student_no':1000, 'GPA': 4.9, 'full_name': 'James'}, "1001":{'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}}
key = "1002"
new_record = remove_a_key(student_record, key)
print(new_record) 





