# Day 10: User Input in Python 🐍🎉

Welcome to Day 10 of the 100 Days of Python Challenge! Today, we will learn about handling user input in Python. Understanding how to take input from users is crucial for creating interactive programs. Let's dive in! 🏊‍♂️

## The `input()` Function 🖥️

The `input()` function is used to take input from the user. It reads a line from the input, converts it into a string, and returns it. Here's a simple example:

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

### Handling Different Data Types 📊

By default, the `input()` function returns a string. If you need to work with other data types, you must convert the input accordingly.

#### String Input

Since `input()` returns a string, no conversion is needed for string inputs:

```python
favorite_color = input("What's your favorite color? ")
print(f"Your favorite color is {favorite_color}.")
```

#### Integer Input

To handle integer input, use the `int()` function to convert the string to an integer:

```python
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
```

#### Float Input

Similarly, for floating-point numbers, use the `float()` function:

```python
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")
```

## Attached Notes 📎

For more detailed explanations and examples, please refer to the attached notes. They contain additional information and exercises to help you master user input in Python.

Happy coding! 🚀