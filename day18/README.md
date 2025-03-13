# Day 18: While Loop in Python 🚀

## Introduction
Welcome to Day 18 of the 100 Days of Python Challenge! Today, we will dive into the concept of the `while` loop in Python. 🐍

## While Loop
A `while` loop in Python repeatedly executes a block of code as long as a given condition is true.

### Syntax
```python
while condition:
    # code block to be executed
```

### Example
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Why Python Doesn't Have `do-while` Loop 🤔
Python does not have a `do-while` loop like some other programming languages (e.g., C, C++, Java). The main reason is that Python emphasizes readability and simplicity, and the `while` loop can achieve the same functionality with a slight modification.

### `do-while` Loop in Other Languages
In languages like C++ or Java, a `do-while` loop ensures that the code block is executed at least once before the condition is tested.

### Example in C++
```cpp
int count = 0;
do {
    cout << count << endl;
    count++;
} while (count < 5);
```

## Simulating `do-while` Loop in Python 🐍
To simulate a `do-while` loop in Python, you can use a `while` loop with a `break` statement.

### Example
```python
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
```

## Notes 📓
- The `while` loop is useful when the number of iterations is not known beforehand.
- Always ensure that the loop has a condition that eventually becomes false to avoid infinite loops.

Happy Coding! 🎉