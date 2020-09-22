from tunde.project.students.student import Student


class StudentTable(Student):

    def create(self, **kwargs):
        return self._add_student(**kwargs)

    def retrieve(self, student_no):
        return self.__get_record(student_no)

    def update(self,student_no,**kwargs):
        return self.__update_student(student_no, **kwargs)

    def delete(self, student_no):
        return self.__delete_record(student_no)

    def write_to_csv(self):
        self.__write_records_to_csv(self._fieldnames, self._table_name)

    def read_from_csv(self):
        return self.__load_records_to_table(self._table_name)