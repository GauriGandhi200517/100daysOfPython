# Day 24 of 100 Days of Python 🐍

## 📚 Topic: Introduction to Tuples in Python

Welcome to Day 24 of the 100 Days of Python Challenge! Today, we dive into **Tuples**, an essential data structure in Python. Tuples are immutable, ordered collections of items, often used to group related data together. Let's explore their features, use cases, and more! 🚀

---

### 🧠 Key Points to Remember

1. **What is a Tuple?**
    - A tuple is a collection of items that is **ordered** and **immutable** (cannot be changed after creation).
    - Tuples are defined using parentheses `()`.

    ```python
    my_tuple = (1, 2, 3)
    ```

2. **Key Characteristics of Tuples**
    - **Immutable**: Once created, the elements of a tuple cannot be modified.
    - **Ordered**: The order of elements is preserved.
    - **Allows Duplicates**: Tuples can contain duplicate values.

3. **Creating Tuples**
    - Empty tuple: `empty_tuple = ()`
    - Single-element tuple: `single_tuple = (42,)` (Note the trailing comma!)
    - Multi-element tuple: `multi_tuple = (1, 2, 3)`

4. **Accessing Tuple Elements**
    - Use indexing to access elements:
      ```python
      my_tuple = (10, 20, 30)
      print(my_tuple[1])  # Output: 20
      ```
    - Negative indexing is also supported:
      ```python
      print(my_tuple[-1])  # Output: 30
      ```

5. **Tuple Operations**
    - **Concatenation**: Combine tuples using `+`.
      ```python
      tuple1 = (1, 2)
      tuple2 = (3, 4)
      result = tuple1 + tuple2  # (1, 2, 3, 4)
      ```
    - **Repetition**: Repeat tuples using `*`.
      ```python
      repeated = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)
      ```

6. **Tuple Methods**
    - `count()`: Returns the number of occurrences of a value.
    - `index()`: Returns the index of the first occurrence of a value.

    Example:
    ```python
    my_tuple = (1, 2, 2, 3)
    print(my_tuple.count(2))  # Output: 2
    print(my_tuple.index(3))  # Output: 3
    ```

7. **Why Use Tuples?**
    - Tuples are faster than lists due to their immutability.
    - They are often used for fixed collections of items, such as coordinates, RGB values, or database records.

8. **Unpacking Tuples**
    - Assign tuple elements to variables in one step:
      ```python
      coordinates = (10, 20)
      x, y = coordinates
      print(x, y)  # Output: 10 20
      ```

---

### 📎 Attached Notes

Make sure to check the attached notes for additional knowledge to solidify your understanding of tuples. These notes include:
 Common pitfalls to avoid when working with tuples.

---

### 🎯 Challenge of the Day

1. Create a tuple with your favorite fruits and print each fruit using a loop.
2. Write a function that takes a tuple of numbers and returns the sum of all elements.
3. Try unpacking a tuple with more elements than variables and handle the error gracefully.

---

### 🌟 Fun Fact

Did you know? Tuples are hashable, which means they can be used as keys in dictionaries, unlike lists! 🗝️

---

Keep practicing and experimenting with tuples to master this versatile data structure. See you tomorrow for Day 25! 🚀

Happy Coding! 😊