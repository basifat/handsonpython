import csv
import os
import sys


def row(student_no, gpa, full_names):
    """ this function creates a dictionary record """
    return dict(student_no=student_no, GPA=gpa, full_names=full_names)


record = {}


def add_row_to_record(row):
    student_info = row["student_no"]
    record[student_info] = row
    return record

# write a function that finds a student(get_student), given the student no as argument and returns row
# if no student was found matching the student number, return the message no student no matching that number on the table


def get_student(student_no):
    """ this function takes in student no and returns found student details"""
    try:
        return record[student_no]
    except KeyError:
        return "no student no matching that number on the table"

# Assignment : update the 'update_student' functions so that it allows us to change either or both of the student GPA or fullnames
# update student (1000, 1.5, Tiger Cruz)
# update student (1001, Roger miller)
# update student(1000, 8.5)

def aggregate_2(student_records):
    """ returns the sum of all student gpa in student records"""
    total = 0
    for record in student_records.values():
        gpa=record["GPA"]
        if gpa > 3.0:
            total += gpa
    return round(total,2)

def average_gpa_2(student_records):
    """ calculete the aerage of all student gpa """
    gpa_total= aggregate_2(student_records)
    extracted_gpa = [record['GPA'] for record in student_records.values() if record["GPA"] > 3]
    return gpa_total/len(extracted_gpa)

def update_student(student_no, **kwargs):
    student_info = record[student_no]
    # print(kwargs)
    if "new_gpa" in kwargs:
        student_info["GPA"] = kwargs["new_gpa"]

    if "new_full_names" in kwargs:
        student_info['full_names'] = kwargs["new_full_names"]
    return student_info

def delete_student(student_no):
    if student_no in record:
        del record[student_no]
    else:
        return "Sorry, it appears that student does not exist in this records."
    return record