# Day 27: Python Challenge - Kaun Banega Crorepati Style Quiz 🎉

Welcome to **Day 27** of the **100 Days of Python Challenge**! Today, we created a fun quiz program inspired by the famous show *Kaun Banega Crorepati* (KBC). 🏆

## Exercise Overview 📚

The task was to create a Python program that:
1. Displays a question with four options.
2. Allows the user to select an answer.
3. Provides feedback on whether the selected answer is correct or not.
4. Includes an option to quit the game.

## Code Explanation 🖥️

Here’s a breakdown of the code and the functions used:

### Code Snippet:
```python
question = "WHO IS THE PRESIDENT OF INDIA?"
print(question)

options = ["A. Dropadi MURMU", "B. NARENDRA MODI", "C. RAHUL GANDHI", "D. MANMOHAN SINGH"]
for i in options:
    print(i)

answer = "A. Dropadi MURMU"
user_input = input("Enter your OPTION: ")

if user_input == "A. Dropadi MURMU":
    print("🎉 CONGRATULATIONS! YOU ARE RIGHT. 🎉")
elif user_input == "B. NARENDRA MODI":
    print("❌ SORRY! YOU ARE WRONG.")
elif user_input == "C. RAHUL GANDHI":
    print("❌ SORRY! YOU ARE WRONG.")
elif user_input == "D. MANMOHAN SINGH":
    print("❌ SORRY! YOU ARE WRONG.")
else:
    print("🤔 USER, DO YOU WANT TO QUIT THE GAME?")
```

### Explanation of Functions and Statements:

1. **`print()`**: Used to display the question and options to the user.
2. **`for` loop**: Iterates through the list of options and prints each one.
3. **`input()`**: Captures the user’s answer.
4. **`if-elif-else` statements**: Checks the user’s input against the correct answer and provides appropriate feedback.

### Features:
- 🎯 **Interactive**: Users can input their answers.
- ✅ **Validation**: The program checks if the answer is correct.
- 🚪 **Exit Option**: Users can quit the game if they wish.

## Happy Coding! 😊
Keep practicing and enjoy your Python journey! 🚀