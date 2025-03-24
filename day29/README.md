# 🐍 Day 29 of 100 Days of Python: Docstrings and PEP 8

Welcome to Day 29 of the **100 Days of Python** challenge! Today, we dive into two essential topics for writing clean, readable, and maintainable Python code: **Docstrings** and **PEP 8**. Let's explore these concepts with examples, a sprinkle of Pythonic wisdom from the Zen of Python. 🧘‍♂️✨

---

## 📜 Docstrings: Documenting Your Code

Docstrings are **multi-line strings** used to document your Python code. They describe what a module, class, or function does, making your code easier to understand for others (and your future self!). Docstrings are enclosed in triple quotes (`"""` or `'''`).

### Why Use Docstrings? 🤔
- Improve code readability 📖
- Provide context for your functions, classes, and modules 🛠️
- Help generate documentation automatically 📚

### Example: Function Docstring
```python
def greet(name):
    """
    Greet the user by their name.

    Args:
        name (str): The name of the user.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"
```

### Example: Class Docstring
```python
class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def add(self, a, b):
        """
        Add two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        return a + b
```

---

## 🧹 PEP 8: The Style Guide for Python Code

PEP 8 is the **official style guide** for Python code. It provides conventions for writing clean and consistent Python code, making it easier to read and collaborate with others.

### Key PEP 8 Guidelines 📝

1. **Indentation**: Use 4 spaces per indentation level.
   ```python
   def example():
       print("Follow PEP 8!")
   ```

2. **Line Length**: Limit lines to 79 characters.
   ```python
   # This is a comment that follows the 79-character limit.
   ```

3. **Blank Lines**: Use blank lines to separate functions, classes, and sections of code.
   ```python
   def function_one():
       pass


   def function_two():
       pass
   ```

4. **Imports**: Place imports at the top of the file and group them logically.
   ```python
   import os
   import sys
   ```

5. **Naming Conventions**:
   - Use `snake_case` for functions and variables.
   - Use `PascalCase` for classes.
   - Use `ALL_CAPS` for constants.

6. **Spaces Around Operators**:
   ```python
   result = 1 + 2  # Add spaces around operators.
   ```

---

## 🧘‍♂️ The Zen of Python

The Zen of Python, written by Tim Peters, is a collection of guiding principles for writing Pythonic code. You can view it by running:

```python
import this
```

### Key Principles to Remember:
- **Beautiful is better than ugly.** ✨
- **Simple is better than complex.** 🧩
- **Readability counts.** 📖

---


## 🎯 Summary

- Use **docstrings** to document your code and make it more understandable.
- Follow **PEP 8** to write clean and consistent Python code.
- Embrace the **Zen of Python** to write Pythonic code.


Happy coding! 🚀🐍