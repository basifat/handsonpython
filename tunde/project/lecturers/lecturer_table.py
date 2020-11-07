from tunde.project.lecturers.lecturer import Lecturer


class LecturerTable(Lecturer):

    def create(self, **kwargs):
        return self.__add_lecturer(**kwargs)

    def retrieve(self, lecturer_no):
        return self.__get_record(lecturer_no)

    def update(self,lecturer_no,**kwargs):
        return self.__update_lecturer(lecturer_no, **kwargs)

    def delete(self, lecturer_no):
        return self.__delete_record(lecturer_no)

    def write_to_csv(self):
        self.__write_records_to_csv(self._fieldnames, self._table_name)

    def read_from_csv(self):
        return self.__load_records_to_table(self._table_name)