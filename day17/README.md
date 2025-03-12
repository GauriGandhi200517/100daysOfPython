# Day 17: Python Loops 🚀

Welcome to Day 17 of the 100 Days of Python Challenge! Today, we will dive into loops in Python, their types, and provide examples of code for better understanding. Let's get started! 🎉

## Types of Loops in Python 🔄

### 1. `for` Loop
The `for` loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) with a definite number of iterations. It is commonly used when the number of iterations is known beforehand.

#### Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
In this example, the loop iterates over each item in the `fruits` list and prints it.

### 2. `while` Loop
The `while` loop is used to execute a block of code as long as a condition is true. It is useful for indefinite iterations where the number of iterations is not known beforehand.

#### Example:
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```
In this example, the loop continues to execute as long as the `count` variable is less than or equal to 5. The `count` variable is incremented by 1 in each iteration.

### 3. Nested Loops
Nested loops are loops within loops. They are used to perform more complex iterations, such as iterating over a matrix or a list of lists.

#### Example:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
```
In this example, the outer loop iterates over each row in the `matrix`, and the inner loop iterates over each item in the current row, printing them in a formatted manner.

## Attached Notes 📎
Please refer to the attached notes for more detailed explanations and additional knowledge  of loops in Python.

Happy coding! 💻