 #Assignment
# Write a an aggregate function that sums the GPA of all students (sum all the GPAs)
# Bonus 1: 
# Do the sum if the GPA is greater than 3.0

# Bonus 2: 
# Write a function that finds the average of the GPA of all students(gpa_sum = 9.85) --> (average = 9.85 / total_no_of_students)


records = {
              "1000": {'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, 
              "1001": {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'},
              "1002": {'student_no': 1001, 'GPA': 2.9, 'full_name': 'Peter'}
          }

def aggregate(student_records):
    total_gpa = sum(record['GPA'] for record in student_records.values() if record["GPA"] > 3) 
    return round(total_gpa, 2)

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


gpa_sum=aggregate_2(records)
print(gpa_sum)

average=average_gpa_2(records)
print(average)


