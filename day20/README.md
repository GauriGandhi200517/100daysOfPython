# Day 20: Functions in Python 🚀

Welcome to **Day 20** of the **100 Days of Python Challenge**! Today, we dive into one of the most fundamental concepts in Python: **Functions**. 🐍

---

## What are Functions? 🤔

Functions are reusable blocks of code that perform a specific task. They help in organizing code, improving readability, and reducing redundancy.

---

## Types of Functions in Python 🛠️

1. **Built-in Functions** 🏗️  
    These are pre-defined functions provided by Python, such as `print()`, `len()`, `type()`, etc.

    ```python
    # Example of a built-in function
    print("Hello, World!")  # Output: Hello, World!
    ```

2. **User-defined Functions** ✍️  
    These are functions created by the user to perform specific tasks.

    ```python
    # Syntax
    def function_name(parameters):
         # Code block
         return value

    # Example
    def greet(name):
         return f"Hello, {name}!"

    print(greet("Alice"))  # Output: Hello, Alice!
    ```

3. **Lambda Functions** ⚡  
    These are anonymous functions defined using the `lambda` keyword. They are typically used for short, simple operations.

    ```python
    # Syntax
    lambda arguments: expression

    # Example
    square = lambda x: x ** 2
    print(square(5))  # Output: 25
    ```

4. **Recursive Functions** 🔄  
    These are functions that call themselves to solve a problem.

    ```python
    # Example
    def factorial(n):
         if n == 0:
              return 1
         else:
              return n * factorial(n - 1)

    print(factorial(5))  # Output: 120
    ```

---

## Notes 📚

- Functions improve code **reusability** and **modularity**.
- Always use meaningful names for functions to enhance readability.
- Use **docstrings** to document your functions.

---

## Attached Notes 📎

Make sure to check the attached notes for more examples and exercises on functions. 📝

Happy coding! 🎉