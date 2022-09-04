# Creating the greatest common denominator algorithm

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))

def gcd(a,b):
    while (b != 0):
        t = a
        a = b
        b = t % b
    return a

# print(gcd(20,8))
# print(gcd(10050, 555))
print("The greatest common denominator of", a, "and", b, "is:", gcd(a, b))
