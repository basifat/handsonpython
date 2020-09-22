from tunde.project.data_handler import DataHandler


class Student(DataHandler):
    
    _table_name = "student.csv"
    _fieldnames = ["entity_id", "gpa", "full_name"]

    def _add_student(self, **kwargs):
        return self._add_record(**kwargs)

    def __update_student(self,entity_id, **kwargs):
        student = self.__get_record(entity_id)
        if "new_gpa" in kwargs:
            student["gpa"] = kwargs["new_gpa"]
        if "new_full_name" in kwargs:
            student["full_name"] = kwargs["new_full_name"]
        return student