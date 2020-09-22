import sys
from Abel.exampleproject.lecturers.lecturer_table import LecturerTable
from Abel.exampleproject.students.student_table import StudentTable

table=LecturerTable()
result=table.create(entity_id=1, full_name="John Bosco", faculty="Business IT", no_of_courses= 2, no_of_student=10, title="Egineer")
print(result)

# table2= StudentTable()
# result2=table2.create(entity_id=1000,new_gpa=6.5)
# print(result2)