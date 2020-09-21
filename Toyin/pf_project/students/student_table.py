from Toyin.pf_project.students.student import Student



class StudentTable(Student):

    def create(self, **kwargs):
        return self.add_student(**kwargs)

    def retrieve(self, student_no):
        return self.get_record(student_no)

    def update(self,student_no,**kwargs):
        return self.update_student(student_no, **kwargs)

    def delete(self, student_no):
        return self.delete_record(student_no)

    def write_to_csv(self): 
        self.write_records_to_csv(self.fieldnames, self.table_name)

    def read_from_csv(self):
        return self.load_records_to_table(self.table_name)