from Toyin.pf_project.data_handler import DataHandler



class Student(DataHandler):
    
    table_name = "student.csv"
    fieldnames = ["entity_id", "gpa", "full_name"]

    def add_student(self, **kwargs):
        return self.add_record(**kwargs)
        
    def update_student(self,entity_id, **kwargs):
        student = self.get_record(entity_id)
        if "new_gpa" in kwargs:
            student["gpa"] = kwargs["new_gpa"]
        if "new_full_name" in kwargs:
            student["full_name"] = kwargs["new_full_name"]
        return student