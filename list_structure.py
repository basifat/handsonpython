# sample = ["red", "blue", "green", "black", "white"]
# first = sample[0]
# print(first)

# second = sample[4]
# print(second)

sample = ["red", "blue", "green", "black", "white"]
cars = ["toyota", "benz"]
sample[3] = "violet"
print(sample)
sample.append("purple")
print(sample)
sample.extend(cars)
print(sample)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8,9]
# Filter the numbers list and return a list of numbers greater than 3  and less than 7
#1. iterate the numbers list
#2. number is greater than 3 and less than 7
#3. return value is a list
#4. print that list
# [4,5,6] 

numbers = [1, 2, 3, 4, 5, 6, 7, 8,9]
new_numbers = []
for number in numbers:
    if (number> 3) and (number < 7):
        new_numbers.append(number)
print(new_numbers)


#numbers = [1, 2, 3, 4, 5, 6, 7, 8,9]
# Everytime we see a number disivisble by 2, we multiply the number by 100
#1. iterate the numbers list
#2. number is a mumtiple of 2, then multiply by 100
#3. return value is a list
#4. print that list
# [1, 200, 3, 400, 5, 600, 7, 800, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8,9]
times_two = []
for number in numbers:
    if (number % 2 == 0):
        number = number * 100 
    times_two.append(number)
print(times_two)

#numbers = [1, 2, 3, 4, 5, 6, 7, 8,9]
# Everytime we see a number disivisble by 2, we multiply the number by 100
#1. iterate the numbers list
#2. number is a mumtiple of 2, then multiply by 100 in place (without assigning to a new variable)
#3. return value is a list
#4. print that list
# [1, 200, 3, 400, 5, 600, 7, 800, 9]

numbers = [1, 2, 3, 4, 5, 6, 7, 8,9]
times_two = []
for number in numbers:
    if (number % 2 == 0):
        number *= 100 
    times_two.append(number)
    print(times_two)


 


