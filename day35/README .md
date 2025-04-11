# 🐍 Day 35: Else in Loops - 100 Days of Python Challenge

Welcome to **Day 35** of the 100 Days of Python Challenge! 🎉 Today, we explored the use of the `else` clause in loops. This is a powerful feature in Python that can make your code more readable and expressive. Let's dive in! 🚀

---

## 🔍 What is `else` in Loops?

In Python, the `else` block in a loop executes **only if the loop completes without encountering a `break` statement**. This can be used to handle scenarios where the loop runs to completion.

---

## 🧑‍💻 Example Code

Here's an example to illustrate how `else` works with loops:

```python
# Searching for a number in a list
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"Found the target: {target} 🎯")
        break
else:
    print(f"Target {target} not found in the list. ❌")
```

### Output:
```
Target 4 not found in the list. ❌
```

In this example:
- The `else` block runs because the loop did not find the target and did not `break`.

---

## 📒 Notes

- The `else` block in loops is **optional**.
- It is commonly used for **search operations** or **validation checks**.
- If the loop is terminated by a `break`, the `else` block will **not execute**.

---

## ✨ Key Takeaways

1. Use `else` in loops to handle cases where the loop completes without interruption.
2. It improves code readability and reduces the need for additional flags or conditions.

---

Happy coding! 🚀 Keep pushing forward in your Python journey! 💪