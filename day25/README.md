# 🐍 Day 25 of 100 Days of Python: Operations on Tuples

Welcome to **Day 25** of the **100 Days of Python Challenge**! 🎉 Today, we explore the essential operations you can perform on **tuples**. Tuples are immutable sequences in Python, making them a great choice for storing data that should not change.

---

## 📚 What are Tuples?

A **tuple** is a collection of ordered elements, enclosed in parentheses `()`. Unlike lists, tuples are **immutable**, meaning their elements cannot be modified after creation.

Example:
```python
my_tuple = (1, 2, 3, "Python", True)
```

---

## ✨ Tuple Operations

Here are the key operations you can perform on tuples:

### 1. **Indexing**
Access tuple elements using their index:
```python
my_tuple = (10, 20, 30)
print(my_tuple[1])  # Output: 20
```

### 2. **Count**
Count the occurrences of a specific element in a tuple:
```python
my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Output: 3
```

### 3. **Index**
Find the index of the first occurrence of an element:
```python
my_tuple = (10, 20, 30, 20)
print(my_tuple.index(20))  # Output: 1
```

---

## 📝 Notes

- Tuples are **immutable**, so you cannot add, remove, or modify elements directly.
- Use tuples when you want to ensure data integrity.
- Tuples can store elements of different data types, including other tuples.

---

## 🚀 Challenge for Today

1. Create a tuple with at least 5 elements.
2. Use the `count` and `index` methods on the tuple.
3. Write a function that takes a tuple and an element as input and returns the index of the element if it exists, or `-1` if it doesn't.

---

Happy coding! 💻✨
