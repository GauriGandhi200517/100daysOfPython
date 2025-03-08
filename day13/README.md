# Day 13: Python Challenge - String Methods

Welcome to Day 13 of the 100 Days of Python Challenge! 🎉 Today, we will explore various string methods in Python. Strings are an essential part of programming, and Python provides a rich set of methods to manipulate them. Let's dive in! 🐍

## String Methods

### 1. `upper()` 🔠
Converts all characters in a string to uppercase.

```python
text = "hello world"
print(text.upper())  # Output: HELLO WORLD
```

### 2. `lower()` 🔡
Converts all characters in a string to lowercase.

```python
text = "HELLO WORLD"
print(text.lower())  # Output: hello world
```

### 3. `capitalize()` 📝
Capitalizes the first character of the string.

```python
text = "hello world"
print(text.capitalize())  # Output: Hello world
```

### 4. `title()` 📚
Capitalizes the first character of each word in the string.

```python
text = "hello world"
print(text.title())  # Output: Hello World
```

### 5. `strip()` ✂️
Removes any leading and trailing whitespace from the string.

```python
text = "   hello world   "
print(text.strip())  # Output: hello world
```

### 6. `replace()` 🔄
Replaces a specified phrase with another specified phrase.

```python
text = "hello world"
print(text.replace("world", "Python"))  # Output: hello Python
```

### 7. `split()` ✨
Splits the string into a list where each word is a list item.

```python
text = "hello world"
print(text.split())  # Output: ['hello', 'world']
```

### 8. `join()` 🔗
Joins the elements of an iterable to the end of the string.

```python
words = ["hello", "world"]
print(" ".join(words))  # Output: hello world
```
Joins the elements of an iterable to the end of the string.

```python
words = ["hello", "world"]
print(" ".join(words))  # Output: hello world
```

## Notes 📓

- String methods do not change the original string; they return a new string.
- Strings in Python are immutable, meaning they cannot be changed after they are created.
- Use these methods to clean, format, and manipulate string data effectively.

Happy coding! 🚀