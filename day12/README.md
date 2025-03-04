# Day 12 of 100 Days of Python 🐍

## Topic: String Slicing and Operations ✂️

Welcome to Day 12 of the 100 Days of Python Challenge! Today, we will dive into string slicing and operations. Strings are an essential part of Python programming, and mastering them will help you manipulate text data efficiently.

### String Slicing 🔪

String slicing allows you to extract a part of a string using a specific range of indices. The syntax for slicing is `string[start:end:step]`.

#### Examples:

```python
# Define a string
my_string = "Hello, World!"

# Slice from index 0 to 4
print(my_string[0:5])  # Output: Hello

# Slice from index 7 to the end
print(my_string[7:])  # Output: World!

# Slice with a step
print(my_string[::2])  # Output: Hlo ol!
```

### String Operations 🔄

Python provides various operations that can be performed on strings, such as concatenation, repetition, and methods for modifying strings.

#### Examples:

```python
# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + ", " + str2 + "!"
print(result)  # Output: Hello, World!

# Repetition
repeat_str = "Python! " * 3
print(repeat_str)  # Output: Python! Python! Python!

# String Methods
upper_str = "hello".upper()
print(upper_str)  # Output: HELLO

lower_str = "WORLD".lower()
print(lower_str)  # Output: world

# Replace
replaced_str = "Hello, World!".replace("World", "Python")
print(replaced_str)  # Output: Hello, Python!
```

### Attached Notes 📎

For more detailed explanations and additional examples, please refer to the attached notes.

Happy coding! 🚀