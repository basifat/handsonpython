""" 
This class implements the abstract methods of 'Base Table', 
and also inherits method from the student class. 
"""
from Abel.exampleproject.students.student import Student

class StudentTable(Student):

    def create(self, **kwargs):
        return self.add_record(**kwargs)

    def retrieve(self, student_no):
        return self.get_record(student_no)

    def update(self,student_no,**kwargs):
        return self.__update_student(student_no, **kwargs)

    def delete(self, student_no):
       return self.delete_record(student_no)

    def write_to_csv(self):
        self.__write_student_to_csv()

    def read_from_csv(self):
        return self.__read_student_records_from_csv()