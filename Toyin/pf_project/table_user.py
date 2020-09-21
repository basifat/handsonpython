# from students.student_table import StudentTable


# example_stable =  StudentTable()
# result = example_stable.create(entity_id=1011, gpa=4.2, full_name="James")
# print(result)


from lecturers.lecturer_table import LecturerTable


example_stable =  LecturerTable()
result = example_stable.create(entity_id= 1, full_name='Tunde', faculty= 'Maths', no_of_courses= 5, no_of_student=20, title= 'Lecturer 1')
print(result)



