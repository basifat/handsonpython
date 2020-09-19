from Abel.exampleproject.data_handler import DataHandler

class Student(DataHandler):
    
    _table_name = "student.csv"
    _fieldnames = ["entity_id", "gpa", "full_name"]

    def add_student(self, **kwargs):
        return self.add_record(**kwargs)
        
         
    def write_student_to_csv(self):
        self.write_record_to_csv(self._fieldnames, self._table_name)

    def read_student_records_from_csv(self):
        return self.load_records_to_table(self._table_name)

    def update_student(self,student_no, **kwargs):
        student = self.get_record(student_no)
        if "new_gpa" in kwargs:
            student["gpa"] = kwargs["new_gpa"]
        if "new_full_name" in kwargs:
            student["full_name"] = kwargs["new_full_name"]
        return student