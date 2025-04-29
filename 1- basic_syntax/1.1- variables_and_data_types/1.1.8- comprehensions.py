# Comprehensions in Python  

# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
even_squares = [x**2 for x in numbers if x % 2 == 0]

# Dictionary comprehension
square_dict = {x: x**2 for x in numbers}

# Set comprehension
unique_squares = {x**2 for x in numbers}

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]

print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")
print(f"Square dictionary: {square_dict}")
print(f"Unique squares: {unique_squares}")
print(f"Flattened matrix: {flattened}")