def fizbuz(number):
    if (number %3==0) and (number%5==0):
        return "FizzBuzz"
    elif (number%3==0):
        return "Fizz"
    elif (number%5 ==0):
        return "Buzz"
    else:
        return number
 

for item in range(1, 51):
    num = fizbuz(item)
    print(num)