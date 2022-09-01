# Tells a user if the string given is a palindrome
# palindrome: reads the same forward as it does backwards

# input a word from user

s = input("Please enter a word: ")
a = s[::-1]
b = s[0:]
if a == b:
    print("This is a palindrome!")
else:
    print("This is not a palindrome :(")
