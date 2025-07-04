# 🕵️‍♂️ Secret Code Decoder

Welcome to **Day 40** of #100DaysOfPython! Today, you'll learn how to create a **Secret Code Decoder** in Python. This project is a fun way to practice string manipulation, loops, and dictionaries.

---

## 🔍 What is a Secret Code Decoder?

A Secret Code Decoder is a tool that translates coded messages into readable text. It's commonly used for:
- **Learning encryption basics**
- **Sending secret messages**
- **Understanding string operations in Python**

---

## 🛠️ How Does It Work?

The decoder uses a simple cipher (like Caesar Cipher or a custom mapping) to convert coded text back to its original form.

**Example:**  
If the code shifts each letter by 3 positions, `D` becomes `A`, `E` becomes `B`, etc.

---

## 🐍 How to Build One in Python

### 1. Choose a Cipher

For beginners, the **Caesar Cipher** is a great start.

### 2. Write the Decoder Function

```python
def decode_caesar_cipher(text, shift):
    decoded = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decoded += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            decoded += char
    return decoded

# Example usage
secret_message = "Khoor Zruog!"  # "Hello World!" shifted by 3
print(decode_caesar_cipher(secret_message, 3))
```

### 3. Test with Your Own Messages

Change the `secret_message` and `shift` to decode different texts.

---

## 💡 What You Learned

- How to manipulate strings in Python
- Basics of encoding and decoding messages
- Using loops and conditionals for text processing

---

## 🚀 Challenge

Try creating your own cipher or add features like:
- Decoding numbers and symbols
- User input for messages and shift values

Happy coding! 🧑‍💻🔐
