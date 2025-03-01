# Day 11: Strings in Python

Welcome to Day 11 of the 100 Days of Python Challenge! Today, we will dive into the fascinating world of strings in Python. Strings are sequences of characters and are one of the most commonly used data types in Python.

## What are Strings? 🤔

In Python, a string is a sequence of characters enclosed within single quotes (`'`), double quotes (`"`), or triple quotes (`'''` or `"""`). Strings are immutable, meaning once they are created, they cannot be changed.

### Types of Strings 📜

1. **Single-line Strings**:
    ```python
    single_line = 'Hello, World!'
    print(single_line)
    ```

2. **Multi-line Strings**:
    ```python
    multi_line = """This is a
    multi-line string."""
    print(multi_line)
    ```

3. **Raw Strings**:
    ```python
    raw_string = r'C:\Users\Name'
    print(raw_string)
    ```

4. **Formatted Strings (f-strings)**:
    ```python
    name = 'Alice'
    age = 30
    formatted_string = f'My name is {name} and I am {age} years old.'
    print(formatted_string)
    ```

## String Operations 🔧

- **Concatenation**:
  ```python
  str1 = 'Hello'
  str2 = 'World'
  result = str1 + ' ' + str2
  print(result)  # Output: Hello World
  ```

- **Repetition**:
  ```python
  str1 = 'Hello'
  result = str1 * 3
  print(result)  # Output: HelloHelloHello
  ```

- **Slicing**:
  ```python
  str1 = 'Hello, World!'
  print(str1[0:5])  # Output: Hello
  ```

- **Length**:
  ```python
  str1 = 'Hello, World!'
  print(len(str1))  # Output: 13
  ```

## Notes 📓

- Strings are immutable.
- Use triple quotes for multi-line strings.
- Use raw strings to handle backslashes in file paths.
- f-strings are a convenient way to format strings.

Happy coding! 🚀