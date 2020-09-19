import os, sys
import csv

from table import Table


class DataHandler(Table):


    def read_from_csv(self):
        raise NotImplementedError

    def write_to_csv(self):
        raise NotImplementedError

    def __get_file_path(self, filename):
        return os.path.join(sys.path[0], filename)

    def __write_records_to_csv(self, fieldnames, table_name):
        path = self.__get_file_path(table_name)
        with open(path, "w", newline="") as f:

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for key in self.records.values():
                writer.writerow(key)
        print(f"Wrote {len(self.records)} records to file.")

    def __load_records_to_table(self, table_name):
        path = self.__get_file_path(table_name)
        with open(path, mode="r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for row in reader:
                self.__add_record(**row)
        return self.records
