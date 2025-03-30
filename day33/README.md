# 🐍 Day 33: Dictionaries in Python - 100 Days of Python Challenge

Welcome to **Day 33** of the **100 Days of Python Challenge**! 🎉 Today, we dive into one of the most versatile and powerful data structures in Python: **Dictionaries**. Let's explore how to access, manipulate, and use dictionaries effectively. 🚀

---

## 📖 What are Dictionaries?

A **dictionary** in Python is a collection of key-value pairs. Each key is unique, and it maps to a specific value. Dictionaries are mutable, meaning you can change their content after creation.

---

## 🔑 Accessing Dictionary Elements

### 1️⃣ Accessing Values by Key
You can access a value in a dictionary using its key:
```python
# Example Dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 25
```

### 2️⃣ Using `.get()` Method
The `.get()` method is a safer way to access values. It avoids errors if the key doesn't exist:
```python
# Using .get()
print(my_dict.get("city"))       # Output: New York
print(my_dict.get("country"))    # Output: None
```

### 3️⃣ Accessing All Keys, Values, and Items
- **Keys**: Use `.keys()` to get all keys.
- **Values**: Use `.values()` to get all values.
- **Items**: Use `.items()` to get key-value pairs.

```python
# Accessing keys, values, and items
print(my_dict.keys())   # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values()) # Output: dict_values(['Alice', 25, 'New York'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])
```

---

## 🛠️ Modifying Dictionaries

### Adding or Updating Key-Value Pairs
```python
# Adding a new key-value pair
my_dict["country"] = "USA"

# Updating an existing key
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}
```

### Removing Key-Value Pairs
- Use `del` to delete a key-value pair.
- Use `.pop()` to remove a key and get its value.

```python
# Deleting a key-value pair
del my_dict["city"]

# Using .pop()
removed_value = my_dict.pop("age")
print(removed_value)  # Output: 26
print(my_dict)        # Output: {'name': 'Alice', 'country': 'USA'}
```

---

## 📝 Notes

1. **Keys must be immutable**: Keys can be strings, numbers, or tuples, but not lists or other dictionaries.
2. **Order is preserved**: Starting from Python 3.7, dictionaries maintain the insertion order.
3. **Efficient lookups**: Dictionaries provide fast access to values using keys.

---

## 🎯 Challenge for Today

1. Create a dictionary to store information about your favorite book (e.g., title, author, year).
2. Write a program to:
    - Add a new key-value pair.
    - Update an existing value.
    - Remove a key-value pair.
    - Print all keys, values, and items.

---

Happy coding! 🚀✨