# 🐍 Day 32 of 100 Days of Python: Set Methods in Python

Welcome to Day 32 of the 100 Days of Python challenge! 🎉 Today, we dive into **Set Methods in Python**. Sets are an unordered collection of unique elements, and Python provides several built-in methods to work with them. Let's explore them with examples! 🚀

---

## 📚 Set Methods Overview

### 1. `add()`
Adds an element to the set.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

---

### 2. `remove()`
Removes a specified element. Raises a `KeyError` if the element is not found.

```python
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}
```

---

### 3. `discard()`
Removes a specified element. Does **not** raise an error if the element is not found.

```python
my_set = {1, 2, 3}
my_set.discard(4)  # No error
print(my_set)  # Output: {1, 2, 3}
```

---

### 4. `pop()`
Removes and returns an arbitrary element from the set.

```python
my_set = {1, 2, 3}
removed_element = my_set.pop()
print(removed_element)  # Output: (varies)
print(my_set)  # Output: Remaining elements
```

---

### 5. `clear()`
Removes all elements from the set.

```python
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()
```

---

### 6. `union()`
Returns a new set containing all elements from both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}
```

---

### 7. `intersection()`
Returns a new set containing only the common elements.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.intersection(set2)
print(result)  # Output: {3}
```

---

### 8. `difference()`
Returns a new set containing elements in the first set but not in the second.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.difference(set2)
print(result)  # Output: {1, 2}
```

---

### 9. `symmetric_difference()`
Returns a new set containing elements not common to both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 2, 4, 5}
```

---

### 10. `issubset()`
Checks if all elements of one set are in another.

```python
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True
```

---

### 11. `issuperset()`
Checks if a set contains all elements of another set.

```python
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True
```

---

### 12. `isdisjoint()`
Checks if two sets have no elements in common.

```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True
```

---

## 📎 Notes
- Sets are **unordered**, so the order of elements may vary.
- Sets do not allow duplicate elements.
- Use `frozenset` for immutable sets.

---

Happy coding! 🧑‍💻 Keep practicing and exploring Python! 💪