# 100 Days of Python Challenge

## **Day 8: Calculator Solution** 🧮

Welcome to Day 8 of the 100 Days of Python Challenge! On this day, we tackled the problem of creating a simple calculator in Python. The calculator can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. Below is a brief explanation of the solution:

1. **Input Handling**: The program takes two numbers and an operator as input from the user.
2. **Operations**: Based on the operator, the program performs the corresponding arithmetic operation.
3. **Output**: The result of the operation is displayed to the user.

Here's a simple example of the calculator in action:

```python
def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"

    print(f"The result is: {result}")

calculator()
```

## **Day 9: Type Casting in Python** 🔄

Welcome to Day 9 of the 100 Days of Python Challenge! On this day, we explored the concept of type casting in Python. Type casting is the process of converting one data type to another. There are two types of type casting:

1. **Implicit Type Casting**: Python automatically converts one data type to another without any user intervention.
2. **Explicit Type Casting**: The user manually converts one data type to another using predefined functions.

### Examples:

**Implicit Type Casting:**

```python
num_int = 10
num_float = 3.14
result = num_int + num_float
print(result)  # Output: 13.14
```

In the above example, Python automatically converts `num_int` to a float before performing the addition.

**Explicit Type Casting:**

```python
num_str = "100"
num_int = int(num_str)
print(num_int)  # Output: 100
```

In this example, we manually convert the string `num_str` to an integer using the `int()` function.

For more details, refer to the attached notes 📑.

Happy coding with Python! 🐍😊

