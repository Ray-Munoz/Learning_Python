# Create an algorithm that prints out the power of a number and the factorial of a number

# The factorial function
def factorial(num):
    if num == 0:
        return 1
    else:
       return num * factorial(num-1)

print("{}! is {}. " .format(10 ,factorial(10)))
