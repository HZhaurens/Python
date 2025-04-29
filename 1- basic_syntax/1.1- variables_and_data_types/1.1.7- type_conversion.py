# Type conversion in Python

# Integer conversion
num_str = "123"
num_int = int(num_str)

# Float conversion
float_str = "3.14"
num_float = float(float_str)

# String conversion
num = 42
str_num = str(num)

# Boolean conversion
bool_str = "True"
bool_val = bool(bool_str)

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# Tuple to set
my_tuple = (1, 2, 2, 3)
my_set = set(my_tuple)

# Dictionary to list of keys
my_dict = {'a': 1, 'b': 2}
keys_list = list(my_dict)

print(f"String to int: {num_int}, type: {type(num_int)}")
print(f"String to float: {num_float}, type: {type(num_float)}")
print(f"Int to string: '{str_num}', type: {type(str_num)}")
print(f"String to bool: {bool_val}, type: {type(bool_val)}")
print(f"List to tuple: {my_tuple}, type: {type(my_tuple)}")
print(f"Tuple to set: {my_set}, type: {type(my_set)}")
print(f"Dict keys to list: {keys_list}, type: {type(keys_list)}")