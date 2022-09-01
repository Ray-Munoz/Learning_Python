# Create a list from two given lists without duplicates

# Given these two lists
a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

# Combine the two lists without duplicates

c = a.union(b)
print(c)
