from student_info import (row, get_student, update_student, add_row_to_record, 
delete_student, aggregate_2, record)
from data import load_csv_to_table, dump_table_to_csv

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