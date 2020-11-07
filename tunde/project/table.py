from tunde.project.base_table import BaseTable


class Table(BaseTable):

    records = {}

    def __get_records(self):
        return self.records

    def __delete_record(self,entity_id):
        if entity_id in self.records:
            del self.records[entity_id]
        else:
            return "Sorry, it appears that record does not exist."
        return self.records
    
    def __get_record(self,entity_id):
        try:
            return self.records[entity_id]
        except KeyError:
            return "No record matching that entity id in the table"

    def __convert_record_info_to_dict(self, **kwargs):
        return dict(**kwargs)
    
    def _add_record(self, **kwargs):
        row = self.__convert_record_info_to_dict(**kwargs)
        entity_id= row["entity_id"]
        self.records[int(entity_id)] = row
        return self.records

    
