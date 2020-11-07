# #Assignment Monday 07/09/2020
# # Write a an aggregate function that sums the GPA of all students (sum all the GPAs)
# # Bonus 1: 
# # Do the sum if the GPA is greater than 3.0

# # Bonus 2: 
# # Write a function that finds the average of the GPA of all students(gpa_sum = 9.85) --> (average = 9.85 / total_no_of_students)


records = {
              "1000": {'student_no': 1000, 'GPA': 4.9, 'full_name': 'James'}, 
              "1001": {'student_no': 1001, 'GPA': 4.95, 'full_name': 'Tale'},
            "1002": {'student_no': 1002, 'GPA': 2.95, 'full_name': 'Sale'}
          }


# #sum the total GPA
def aggregate(records):
    list_of_gpa= ({key:values['GPA'] for key,values in records.items()})
    return(sum(list_of_gpa.values()))

sum_of_gpa = aggregate(records)
print(sum_of_gpa)



#sum of GPA greater than 3.0
def aggregate_greater_than3(records):
    list_of_gpa= ({key:values['GPA'] for key,values in records.items()})
    return sum(values for values in list_of_gpa.values() if values > 3.0)
    
sum_of_gpa_greater_than3 = aggregate_greater_than3(records)
print(sum_of_gpa_greater_than3)


#the example i looked at to get the answer for greater than 3
# a_dict = {"a":1, "b":2, "c": 3} 
# sum(v for v in a_dict.values() if v > 2)

# average of GPA
def aggregate_average(records):
    list_of_gpa= ({key:values['GPA'] for key,values in records.items()})
    average = (sum(list_of_gpa.values()))/len(list_of_gpa)
    return average

average_of_gpa = aggregate_average(records)
print(average_of_gpa)



