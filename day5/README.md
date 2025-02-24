# Day 5 of 100 Days of Python
Welcome to Day 5 of 100 Days of Python! 🎉

Today, we will be covering the following topics:
- Comments in Python
- Escape Sequence Characters
- The `print` Function

Let's dive in and enhance our Python skills!

## Comments in Python

Comments are used to explain code and make it more readable. Python supports two types of comments:

1. **Single-line comments**: These start with the `#` symbol.
    ```python
    # This is a single-line comment
    print("Hello, World!")
    ```

2. **Multi-line comments**: These can be created using triple quotes (`'''` or `"""`).
    ```python
    """
    This is a multi-line comment.
    It spans multiple lines.
    """
    print("Hello, World!")
    ```

## Escape Sequence Characters

Escape sequences are used to represent certain special characters within strings. Some common escape sequences are:

- `\n` : Newline
- `\t` : Tab
- `\\` : Backslash
- `\'` : Single quote
- `\"` : Double quote

Example:
```python
print("Hello\nWorld")  # Prints "Hello" and "World" on separate lines
print("Hello\tWorld")  # Prints "Hello" and "World" separated by a tab
```

## The `print` Function

The `print` function is used to output text to the console. It has several optional parameters, including `sep` and `end`.

- `sep`: Specifies the separator between multiple arguments. Default is a space.
- `end`: Specifies what to print at the end. Default is a newline.

Example:
```python
print("Hello", "World", sep="🌍")  # Prints "Hello🌍World"
print("Hello", end="👋")          # Prints "Hello" followed by "👋" instead of a newline
print("World")
```

## Using Triple Quotes

Triple quotes (`'''` or `"""`) are used for multi-line strings and docstrings.

Example:
```python
multi_line_string = """This is a string
that spans multiple
lines."""
print(multi_line_string)
```

Triple quotes can also be used for multi-line comments, as shown earlier.

## Attached Notes

Please refer to the attached notes for additional information and examples related to today's topics.

## Summary

- Use `#` for single-line comments.
- Use `'''` or `"""` for multi-line comments.
- Use escape sequences like `\n`, `\t`, etc., to represent special characters.
- Customize the `print` function with `sep` and `end` parameters.

Happy coding! 🚀🐍