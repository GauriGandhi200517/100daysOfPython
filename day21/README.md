# 🐍 Day 21: Functional Arguments in Python

Welcome to **Day 21** of the **100 Days of Python Challenge**! Today, we dive into the fascinating world of **functional arguments** in Python. 🚀

---

## 📚 What Are Functional Arguments?

In Python, **functional arguments** are the inputs we pass to functions to customize their behavior. They allow us to make our functions dynamic and reusable. Understanding the types of arguments and how to use them effectively is crucial for writing clean and efficient code.

---

## 🛠️ Types of Functional Arguments

1. **Positional Arguments**  
    These are the most common type of arguments. The order in which they are passed matters.  
    **Syntax:**  
    ```python
    def greet(name, age):
         print(f"Hello {name}, you are {age} years old!")

    greet("Alice", 25)  # Output: Hello Alice, you are 25 years old!
    ```

2. **Keyword Arguments**  
    These are arguments passed by explicitly specifying the parameter name. The order does not matter.  
    **Syntax:**  
    ```python
    def greet(name, age):
         print(f"Hello {name}, you are {age} years old!")

    greet(age=25, name="Alice")  # Output: Hello Alice, you are 25 years old!
    ```

3. **Default Arguments**  
    These are arguments that have default values. If no value is provided, the default is used.  
    **Syntax:**  
    ```python
    def greet(name, age=18):
         print(f"Hello {name}, you are {age} years old!")

    greet("Alice")  # Output: Hello Alice, you are 18 years old!
    ```

4. **Variable-Length Arguments**  
    These allow you to pass a variable number of arguments to a function.  
    - **`*args`** for non-keyword arguments:  
      ```python
      def add_numbers(*args):
            return sum(args)

      print(add_numbers(1, 2, 3, 4))  # Output: 10
      ```
    - **`**kwargs`** for keyword arguments:  
      ```python
      def print_info(**kwargs):
            for key, value in kwargs.items():
                 print(f"{key}: {value}")

      print_info(name="Alice", age=25)  
      # Output:
      # name: Alice
      # age: 25
      ```

---

## 📝 Notes

- Positional arguments must appear before keyword arguments.
- Use `*args` and `**kwargs` to make your functions flexible and adaptable.
- Default arguments should be used cautiously to avoid unexpected behavior.

---

## 💡 Key Takeaways

- Functional arguments are essential for writing reusable and dynamic functions.
- Understanding the types of arguments helps in designing better APIs and code structures.

---

Happy coding! 🎉 Keep pushing forward in your Python journey! 💪