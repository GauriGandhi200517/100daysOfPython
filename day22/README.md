# Day 22: Introduction to Lists in Python 🐍📋

Welcome to **Day 22** of the **100 Days of Python Challenge**! 🎉 Today, we dive into one of the most versatile and commonly used data structures in Python: **Lists**. 🚀

---

## What are Lists? 🤔

A **list** in Python is a collection of items that are ordered, changeable (mutable), and allow duplicate values. Lists are one of the most powerful tools in Python for storing and manipulating data.

### Key Features of Lists:
- **Ordered**: Items have a defined order that will not change unless explicitly modified.
- **Mutable**: You can add, remove, or modify items.
- **Heterogeneous**: Lists can store items of different data types (e.g., integers, strings, floats, etc.).
- **Duplicates Allowed**: Lists can contain duplicate values.

---

## Creating a List 🛠️

Here’s how you can create a list in Python:

```python
# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# A list with mixed data types
mixed_list = [42, "Python", 3.14, True]
print(mixed_list)  # Output: [42, 'Python', 3.14, True]
```

---

## Accessing List Elements 🔍

You can access elements in a list using **indexing** (starting from 0):

```python
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

# Negative indexing
print(fruits[-1])  # Output: cherry
```

---

## Modifying a List ✏️

Lists are mutable, so you can modify their contents:

```python
numbers = [10, 20, 30, 40]

# Changing an element
numbers[1] = 25
print(numbers)  # Output: [10, 25, 30, 40]

# Adding elements
numbers.append(50)
print(numbers)  # Output: [10, 25, 30, 40, 50]

# Removing elements
numbers.remove(30)
print(numbers)  # Output: [10, 25, 40, 50]
```

---

## Common List Operations 🛠️

Here are some useful operations you can perform on lists:

```python
# List of numbers
nums = [1, 2, 3, 4, 5]

# Length of the list
print(len(nums))  # Output: 5

# Check if an item exists
print(3 in nums)  # Output: True

# Slicing a list
print(nums[1:4])  # Output: [2, 3, 4]

# Reversing a list
nums.reverse()
print(nums)  # Output: [5, 4, 3, 2, 1]

# Sorting a list
nums.sort()
print(nums)  # Output: [1, 2, 3, 4, 5]
```

---

## Why Use Lists? 🤷‍♂️

Lists are incredibly versatile and can be used in a variety of scenarios, such as:
- Storing a collection of related data (e.g., names, scores, etc.).
- Iterating through items using loops.
- Performing complex operations like filtering, mapping, and reducing.

---

## Practice Time! 🏋️‍♂️

Try solving these challenges to solidify your understanding of lists:
1. Create a list of your favorite movies and print them one by one.
2. Write a program to find the largest number in a list.
3. Reverse a list without using the `reverse()` method.

---

That’s it for today! 🎉 Keep practicing, and you’ll master Python lists in no time. See you tomorrow for another exciting topic! 🚀

Happy Coding! 💻✨