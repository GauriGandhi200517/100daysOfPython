# Day 3 of 100 Days of Python Challenge
Welcome to Day 3 of the 100 Days of Python Challenge!

# Day 3 of 100: Modules and PIP 📦

## What are Modules? 🧩
Modules are files containing Python code that can be imported and used in other Python programs. They help in organizing code into manageable sections.

### Types of Modules
1. **Built-in Modules**: These are pre-installed with Python. Examples include `math`, `sys`, and `os`.
    ```python
    import math
    print(math.sqrt(16))  # Output: 4.0
    ```

2. **External Modules**: These are not included with Python and need to be installed separately using PIP. Examples include `pandas` and `scikit-learn`.
    ```python
    import pandas as pd
    data = pd.read_csv('data.csv')
    print(data.head())
    ```

## PIP: Python Package Installer 📥
PIP is a package manager for Python that allows you to install and manage additional libraries and dependencies that are not included in the standard library.

### Installing a Package
To install a package using PIP, use the following command:
```sh
pip install package_name
```
For example, to install `pandas`:
```sh
pip install pandas
```

## Popular External Modules
- **Pandas**: A powerful data manipulation and analysis library.
- **Scikit-learn**: A machine learning library for Python.

## Working with CSV Files 📑
CSV (Comma-Separated Values) files are commonly used to store tabular data. You can use the `pandas` library to read and write CSV files easily.
```python
import pandas as pd
data = pd.read_csv('data.csv')
print(data.head())
```

For more details, refer to the attached notes.

Happy Coding! 🚀