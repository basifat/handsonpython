#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Sum all the numbers in the 'numbers' list and print the sum.
# loop through the list
# Add the numbers as we are looping through
# Print the total sum at the end of the loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0

for number in numbers:
    total = number + total
print(total)


#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Find the minimum number in the list and the print that number.
# output = 1
# loop through the numbers
# keep track the minimum number
# print the number

numbers = [3, 7, 4, 5, 6, 8, 9, 2]
minimum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number
print(minimum)

# minimum = 9
# number = 1
# 1  <  9,
# mimimum = 1
# number =2
# 2 < 1
# mimimum = 1


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers_updated = [number+2 for number in numbers]
print(numbers_updated)
# total = 0

# for number in numbers:
#     total = number + total
# print(total)









