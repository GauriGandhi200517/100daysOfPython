# 🐍 30 Days Out of 100 Days of Python Challenge: Recursion

Welcome to Day 30 of the **100 Days of Python Challenge**! 🎉 Today, we explored the fascinating concept of **Recursion**. Let's dive in! 🚀

---

## 🔄 What is Recursion?

Recursion is a programming technique where a function calls itself to solve smaller instances of a problem. It is particularly useful for problems that can be broken down into smaller, similar sub-problems. 🧩

### Example: Factorial Calculation

The factorial of a number `n` is the product of all positive integers less than or equal to `n`. For example, `5! = 5 × 4 × 3 × 2 × 1`. 🧮

Here's how we can calculate it using recursion:

```python
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call

# Test the function
print(factorial(5))  # Output: 120
```

---

## 🌀 Fibonacci Series

The **Fibonacci series** is a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The sequence looks like this: `0, 1, 1, 2, 3, 5, 8, 13, ...`. 🔢

### Example: Fibonacci Series Using Recursion

```python
def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

# Print the first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34
```

---

## 🌟 Key Takeaways

- Recursion is a powerful tool for solving problems that can be divided into smaller sub-problems. 🛠️
- Always define a **base case** to prevent infinite recursion. 🚨
- Be cautious of performance issues with deep recursion, as it can lead to stack overflow. ⚠️

Happy Coding! 💻✨