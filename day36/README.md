# 🐍 Day 36: Exception Handling in Python

Welcome to **Day 36** of the **100 Days of Python Challenge**! 🎉 Today, we explored the powerful concept of **Exception Handling** in Python. Let's dive into the details! 🚀

---

## 🌟 What is Exception Handling?

Exception handling in Python allows you to gracefully handle errors that occur during the execution of your program. Instead of crashing, your program can respond to errors in a controlled way.

---

## 🛠️ Syntax of Exception Handling

Here’s the basic syntax for handling exceptions in Python:

```python
try:
    # Code that might raise an exception
    risky_operation()
except SomeException as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
else:
    # Code to execute if no exception occurs
    print("Operation successful!")
finally:
    # Code that will always execute
    print("Execution complete.")
```

---

## 📖 Code Examples

### Example 1: Handling a ZeroDivisionError
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Division attempt finished.")
```

### Example 2: Handling Multiple Exceptions
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Program execution complete.")
```

---

## 📌 Key Notes

- Use `try` to wrap the code that might raise exceptions.
- Use `except` to handle specific exceptions.
- The `else` block runs only if no exceptions occur.
- The `finally` block always executes, regardless of exceptions.

---

## 📝 Attached Notes

Make sure to review the attached notes for additional insights and best practices on exception handling. 📂

---

Keep practicing exception handling to make your Python programs more robust and error-resistant! 💪

Happy Coding! 😊