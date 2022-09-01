# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# generating a random list
import random

#Generate 10 random numbers between 1 and 100000
randomlist = random.sample(range(1, 100000), 10)
print('This is a randomly generated list: ', randomlist)

print('These are all the even numbers within the list: ')
for n in randomlist:
    if n % 2 == 0:
        print(n, end = '\t')
