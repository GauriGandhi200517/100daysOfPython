# Day 14: If-Else Conditional Statements in Python 🐍

Welcome to Day 14 of the 100 Days of Python Challenge! 🎉 Today, we will dive into the world of if-else conditional statements. Conditional statements are fundamental in programming as they allow you to execute certain pieces of code based on specific conditions.

## What are If-Else Statements?

If-else statements are used to perform different actions based on different conditions. The basic syntax is:

```python
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
```

## Types of Conditional Statements

### 1. Simple If Statement

The `if` statement evaluates a condition and executes the code block if the condition is true.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### 2. If-Else Statement

The `if-else` statement provides an alternative code block to execute if the condition is false.

```python
x = 10
if x > 15:
    print("x is greater than 15")
else:
    print("x is not greater than 15")
```

### 3. Elif Statement

The `elif` (short for else if) statement allows you to check multiple conditions.

```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")
```

### 4. Nested If Statements

You can nest if statements within other if statements to check multiple conditions.

```python
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is 15 or more")
else:
    print("x is 5 or less")
```

## Summary

For more detailed explanations and examples, refer to the attached notes. 📚

Happy coding! 🚀🐍



