# 🐍 Day 34 of 100 Days of Python: Dictionary Methods in Python

Welcome to Day 34 of the **100 Days of Python Challenge**! 🎉 Today, we explored the powerful and versatile **dictionary methods** in Python. Below is a comprehensive guide to all the methods we covered, complete with examples. 📚

---

## 📖 Dictionary Methods Overview

### 1. `dict.clear()`
Removes all items from the dictionary.

```python
my_dict = {"a": 1, "b": 2, "c": 3}
my_dict.clear()
print(my_dict)  # Output: {}
```

---

### 2. `dict.copy()`
Returns a shallow copy of the dictionary.

```python
original = {"x": 10, "y": 20}
copy_dict = original.copy()
print(copy_dict)  # Output: {'x': 10, 'y': 20}
```

---

### 3. `dict.fromkeys(iterable, value)`
Creates a new dictionary with keys from the iterable and a single value.

```python
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
```

---

### 4. `dict.get(key, default)`
Returns the value for the specified key if it exists, otherwise returns the default value.

```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("gender", "Not specified"))  # Output: Not specified
```

---

### 5. `dict.items()`
Returns a view object of the dictionary's key-value pairs.

```python
my_dict = {"a": 1, "b": 2}
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])
```

---

### 6. `dict.keys()`
Returns a view object of the dictionary's keys.

```python
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])
```

---

### 7. `dict.pop(key, default)`
Removes the specified key and returns its value. If the key is not found, returns the default value.

```python
my_dict = {"a": 1, "b": 2}
value = my_dict.pop("a")
print(value)  # Output: 1
print(my_dict)  # Output: {'b': 2}
```

---

### 8. `dict.popitem()`
Removes and returns the last inserted key-value pair as a tuple.

```python
my_dict = {"a": 1, "b": 2}
item = my_dict.popitem()
print(item)  # Output: ('b', 2)
print(my_dict)  # Output: {'a': 1}
```

---

### 9. `dict.setdefault(key, default)`
Returns the value of the key if it exists; otherwise, inserts the key with the default value.

```python
my_dict = {"a": 1}
value = my_dict.setdefault("b", 2)
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'b': 2}
```

---

### 10. `dict.update([other])`
Updates the dictionary with key-value pairs from another dictionary or iterable.

```python
my_dict = {"a": 1}
my_dict.update({"b": 2, "c": 3})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

---

### 11. `dict.values()`
Returns a view object of the dictionary's values.

```python
my_dict = {"a": 1, "b": 2}
print(my_dict.values())  # Output: dict_values([1, 2])
```

---

## 📎 Attached Notes
Make sure to check out the detailed notes in this directory for additional examples and explanations! 📝

---

## 🌟 Key Takeaways
- Dictionaries are incredibly versatile and efficient for storing key-value pairs.
- Python provides a rich set of methods to manipulate and interact with dictionaries.
- Practice these methods to master dictionary operations! 💪

Happy Coding! 🚀