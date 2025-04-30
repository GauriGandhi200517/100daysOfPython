# Day 37 of 100 Days of Python 🐍: Understanding the `final` Keyword in Python 🚀  

Welcome to Day 37! Today, we explored the `final` keyword in Python, which is used to enforce immutability and prevent modifications in certain scenarios. Let's dive in!  

---

## What is the `final` Keyword? 🔒  

The `final` keyword is part of Python's `typing` module. It is used to:  
1. **Prevent inheritance** of a class.  
2. **Prevent overriding** of methods in subclasses.  
3. **Indicate constants** (though Python doesn't enforce immutability).  

---

## How to Use the `final` Keyword? 🛠️  

### 1. Preventing Class Inheritance  
```python  
from typing import final  

@final  
class BaseClass:  
    pass  

class DerivedClass(BaseClass):  # ❌ TypeError: BaseClass is final  
    pass  
```  

### 2. Preventing Method Overriding  
```python  
from typing import final  

class Parent:  
    @final  
    def important_method(self):  
        print("This method cannot be overridden!")  

class Child(Parent):  
    def important_method(self):  # ❌ TypeError: important_method is final  
        print("Trying to override!")  
```  

### 3. Indicating Constants  
```python  
from typing import final  

PI: final = 3.14159  
PI = 3.14  # ⚠️ No error, but discouraged as PI is marked final.  
```  

---

## When to Use the `final` Keyword? 🤔  

- Use `@final` on classes or methods to **enforce strict design rules** and prevent unintended inheritance or overriding.  
- Use `final` for variables to **signal intent** that they should not be reassigned, improving code clarity.  

---

## Key Takeaways 📝  

- The `final` keyword is a **design tool** to enforce immutability and prevent modification.  
- It helps in creating **robust and predictable codebases**.  
- While Python doesn't enforce immutability for variables, marking them as `final` serves as a **clear signal** to other developers.  

---

Happy coding! 🎉  