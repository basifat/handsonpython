# def get_dict_wo_key(dictionary, key):
#     """Returns a **shallow** copy of the dictionary without a key."""
#     _dict = dictionary.copy()
#     _dict.pop(key, None)
#     return _dict



# d = {"1000": {'student_no':1000, 'GPA': 4.9, 'full_name': 'James'}, "1001":{'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}}
# key_to_remove = "1000"
# new_d = get_dict_wo_key(d, key_to_remove)
# print(new_d)  # {"a": [1, 2, 3], "b": 2}



# # new_d["a"].append(100)
# # print(d)  # {"a": [1, 2, 3, 100], "b": 2, "c": 3}
# # print(new_d)  # {"a": [1, 2, 3, 100], "b": 2}
# # new_d["b"] = 2222
# # print(d)  # {"a": [1, 2, 3, 100], "b": 2, "c": 3}
# # print(new_d)  # {"a": [1, 2, 3, 100], "b": 2222}




# def delete_student_record(dictionary, key):
#     recordz = dictionary.copy()
#     recordz.pop(key, None)
#     return recordz



# student_record= {"1000": {'student_no':1000, 'GPA': 4.9, 'full_name': 'James'}, "1001":{'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}}
# key_to_remove = "1000"
# new_record = delete_student_record(student_record, key_to_remove)
# print(new_record) 

# def get_student(student_no):
#     try:
#         return records[student_no]
#     except KeyError:
#         return "No student matching that student no in the table"

# def remove_a_key(records, key):
#     recordz = dict(records)
#     try:
#         del recordz[key]
#         return recordz
#     except KeyError:
#         return "Sorry, it appears that student does not exist"


# student_record= {"1000": {'student_no':1000, 'GPA': 4.9, 'full_name': 'James'}, "1001":{'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}}
# key = "1002"
# new_record = remove_a_key(student_record, key)
# print(new_record)  


def delete_student_record(records, key):
    recordz = records.copy()
    try:
        recordz.pop(key, None)
        return recordz
    except:
        return "Sorry, it appears that student does not exist in this record"
    

student_record= {"1000": {'student_no':1000, 'GPA': 4.9, 'full_name': 'James'}, "1001":{'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'}}
key = "1002"
new_record = delete_student_record(student_record, key)
print(new_record) 




