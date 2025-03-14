# Day 19: Break and Continue Statements 🚀

Welcome to **Day 19** of the **100 Days of Python Challenge**! Today, we explore two powerful control flow tools in Python: `break` and `continue`. These statements help you manage loops effectively. Let's dive in! 🐍✨

---

## 🔹 Break Statement 🛑
The `break` statement allows you to exit a loop prematurely when a specific condition is met.

### Example:
```python
# Example: Using break in a loop
for number in range(1, 10):
    if number == 5:
        print("Breaking the loop at number:", number)
        break
    print(number)
```

**Output:**
```
1
2
3
4
Breaking the loop at number: 5
```

### 📝 Notes:
- The `break` statement **terminates the loop entirely**.
- It is often used when you need to stop searching after finding a specific value or condition.

---

## 🔹 Continue Statement ⏭️
The `continue` statement skips the current iteration of the loop and proceeds to the next one.

### Example:
```python
# Example: Using continue in a loop
for number in range(1, 10):
    if number % 2 == 0:
        continue  # Skip even numbers
    print(number)
```

**Output:**
```
1
3
5
7
9
```

### 📝 Notes:
- The `continue` statement **does not terminate the loop**; it only skips the current iteration.
- It is useful for **ignoring unwanted values** or conditions during iteration.

---

## 🌟 Key Takeaways 💡
- Use `break` to **exit a loop** when a condition is met. 🛑
- Use `continue` to **skip specific iterations** in a loop. ⏭️
- Both statements make your loops more **efficient** and **readable**.

---

Happy coding! 🎉 Keep experimenting with these statements to level up your Python skills. 💻🐍