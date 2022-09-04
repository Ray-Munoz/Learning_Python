# Create an algorithm that prints out the power of a number and the factorial of a number

calculate_factorial_or_power = input("Do you want to find the factorial or power of a number? Type factorial/power: ")


# The factorial function
def factorial(num):
    if num == 0:
        return 1
    else:
       return num * factorial(num-1)
# The power function
def power(x, pwr):
    if pwr == 0:
        return 1
    else:
        return x * power(x, pwr-1)

if calculate_factorial_or_power == "factorial":
    num = int(input("Enter a number to find its factorial: "))
    print("{}! is {}. " .format(num, factorial(num)))
elif calculate_factorial_or_power == "power":
    x = int(input("Enter a base number: "))
    pwr = int(input("Enter an exponent number: "))
    print("{} to the power of {} is {} " .format(x, pwr, power(x,pwr)))


# print("{}! is {}. " .format(10, factorial(10)))
# print("{} to the power of {} is {} " .format(10, 3, power(10,3)))
