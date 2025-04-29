# List operations in Python

# Creating lists
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
mixed = [1, 'hello', 3.14, True]

# Accessing elements
first_num = numbers[0]
last_fruit = fruits[-1]

# Slicing
sub_list = numbers[1:4]

# Modifying lists
fruits.append('grape')
fruits.insert(1, 'pear')
fruits.remove('banana')

# List methods
length = len(numbers)
sorted_fruits = sorted(fruits)
reversed_numbers = numbers[::-1]


print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"First number: {first_num}, Last fruit: {last_fruit}")
print(f"Sub list: {sub_list}")
print(f"Modified fruits: {fruits}")
print(f"Length: {length}, Sorted: {sorted_fruits}, Reversed: {reversed_numbers}")
