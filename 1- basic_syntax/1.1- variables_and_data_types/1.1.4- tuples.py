# Tuple operations in Python

# Creating tuples
coordinates = (10, 20)
colors = ('red', 'green', 'blue')
single_element = (42,)

# Accessing elements
x = coordinates[0]
last_color = colors[-1]

# Slicing
sub_colors = colors[1:3]

# Tuple unpacking
x, y = coordinates

# Tuple methods
length = len(colors)
index = colors.index('green')
count = colors.count('red')

# Tuple vs list
# Tuples are immutable
# colors[0] = 'yellow'  # This will raise an error

print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"First coordinate: {x}, Last color: {last_color}")
print(f"Sub colors: {sub_colors}")
print(f"Unpacked: x={x}, y={y}")
print(f"Length: {length}, Index of 'green': {index}, Count of 'red': {count}")