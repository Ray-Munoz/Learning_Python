# Ask the user for a number and determine whether the number is prime or not.


# Creating a divisor function
def divisors(num):
    list_of_num = range(1, num+1)
    list_of_divisors = []
    for n in list_of_num:
        if num % n == 0:
            list_of_divisors.append(n)
    return list_of_divisors


# Determining if a number is prime
num = int(input("Enter a number: "))
if (len(divisors(num)) <= 2):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
