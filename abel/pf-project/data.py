import csv
import os
import sys
from student_info import add_row_to_record
def get_file_path(filename):
    return os.path.join(sys.path[0], filename)



def load_csv_to_table(source_file):
    get_file_path(source_file)
    with open(source_file,mode="r") as csv_file:
        reader = csv.DictReader(csv_file,delimiter=",")
        for row in reader:
            add_row_to_record(row)

def dump_table_to_csv(output_file, table):
    get_file_path(output_file)
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['student_no', 'GPA', 'full_names']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key in table.values():
            writer.writerow(key)
