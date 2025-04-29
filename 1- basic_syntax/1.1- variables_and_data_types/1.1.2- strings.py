# String operations in Python

# Basic string
s = "Hello World"

# String concatenation
s1 = "Hello"
s2 = "World"
combined = s1 + " " + s2

# String indexing
first_char = s[0]
last_char = s[-1]

# String slicing
substring = s[0:5]

# String methods
lower_case = s.lower()
upper_case = s.upper()
stripped = "  hello  ".strip()

# String formatting
name = "Alice"
age = 25
formatted = f"My name is {name} and I'm {age} years old."

# Advanced string formatting
# Using format() method
formatted2 = "My name is {} and I'm {} years old.".format(name, age)

# Using % operator
formatted3 = "My name is %s and I'm %d years old." % (name, age)

# Regular expressions
import re
pattern = r"\b[A-Za-z]+\b"
matches = re.findall(pattern, s)

# String encoding
text = "你好"
utf8_bytes = text.encode('utf-8')
decoded_text = utf8_bytes.decode('utf-8')

print(f"Original string: {s}")
print(f"Concatenated: {combined}")
print(f"First character: {first_char}, Last character: {last_char}")
print(f"Substring: {substring}")
print(f"Lower case: {lower_case}, Upper case: {upper_case}")
print(f"Stripped: '{stripped}'")
print(f"Formatted: {formatted}")
print(f"Format method: {formatted2}")
print(f"Percent formatting: {formatted3}")
print(f"Regex matches: {matches}")
print(f"UTF-8 bytes: {utf8_bytes}")
print(f"Decoded text: {decoded_text}")