# 🐍 Day 38: Raising Custom Errors in Python 🚨

Welcome to **Day 38** of the **100 Days of Python Challenge**! 🎉 Today, we explored the concept of **raising custom errors** in Python. This is an essential skill for writing robust and user-friendly code. Let's dive into the details! 🔍

---

## 📖 What We Learned

### 🔥 Raising Custom Errors
In Python, we can raise exceptions using the `raise` keyword. Custom errors allow us to define our own exception classes, making it easier to handle specific error scenarios in our programs.

### 🛠️ Example Code
```python
class CustomError(Exception):
    """A custom exception class."""
    pass

def check_value(value):
    if value < 0:
        raise CustomError("Value cannot be negative!")
    return f"Value is valid: {value}"

try:
    print(check_value(-5))
except CustomError as e:
    print(f"Custom Error Caught: {e}")
```

**Explanation**:
1. We define a custom exception class `CustomError` by inheriting from the built-in `Exception` class.
2. The `check_value` function raises `CustomError` if the input value is negative.
3. The `try-except` block catches the custom error and handles it gracefully.

---

## 📋 Notes
📌 **Attached Notes**: Detailed notes on raising custom errors, including best practices and real-world use cases, are included in the project directory. Make sure to review them for a deeper understanding! 📝

---

## ✨ Summary
- Custom errors improve code readability and maintainability. ✅
- They allow us to handle specific error scenarios effectively. 💡
- Always document your custom exceptions for better collaboration. 📚

---

🎯 **Challenge Completed!** Keep up the great work, and see you on Day 39! 🚀