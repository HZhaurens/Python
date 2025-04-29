# Set operations in Python

# Creating sets
fruits = {'apple', 'banana', 'orange'}
numbers = {1, 2, 3, 4, 5}

# Adding elements
fruits.add('grape')

# Removing elements
fruits.remove('banana')

# Set operations
colors1 = {'red', 'green', 'blue'}
colors2 = {'blue', 'yellow', 'green'}

union = colors1 | colors2
intersection = colors1 & colors2
difference = colors1 - colors2

# Set methods
length = len(fruits)
contains = 'apple' in fruits

# Set comprehension
squares = {x**2 for x in range(1, 6)}

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Union: {union}, Intersection: {intersection}, Difference: {difference}")
print(f"Length: {length}, Contains 'apple': {contains}")
print(f"Squares: {squares}")