from tunde.project.data_handler import DataHandler


class Lecturer(DataHandler):

    _table_name = "lecturer.csv"
    _fieldnames = ['entity_id', 'full_name', 'faculty', 'no_of_courses', 'no_of_student', 'title']
    
    
    def __add_lecturer(self, **kwargs):
        return self.__add_record(**kwargs)
        
    def __update_lecturer(self, entity_id,**kwargs):
        lecturer_info = self.records[entity_id]
        if "updated_courses" in kwargs:
            lecturer_info["no_of_courses"] = kwargs["updated_courses"]

        if "updated_no_student" in kwargs:
            lecturer_info['no_of_student'] = kwargs["updated_no_student"]
        return lecturer_info