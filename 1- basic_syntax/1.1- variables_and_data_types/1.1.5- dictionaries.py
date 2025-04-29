# Dictionary operations in Python

# Creating dictionaries
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
squares = {1: 1, 2: 4, 3: 9, 4: 16}

# Accessing values
name = person['name']
age = person.get('age')

# Modifying dictionaries
person['age'] = 26
person['job'] = 'Engineer'

# Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()

# Dictionary comprehension
square_dict = {x: x**2 for x in range(1, 6)}

# Advanced dictionary operations
# Dictionary merging
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}

# Nested dictionaries
nested = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}

# defaultdict usage
from collections import defaultdict
dd = defaultdict(int)
dd['count'] += 1

print(f"Person: {person}")
print(f"Squares: {squares}")
print(f"Name: {name}, Age: {age}")
print(f"Modified person: {person}")
print(f"Keys: {list(keys)}, Values: {list(values)}, Items: {list(items)}")
print(f"Square dict: {square_dict}")
print(f"Merged dictionary: {merged}")
print(f"Nested dictionary: {nested}")
print(f"Defaultdict: {dict(dd)}")