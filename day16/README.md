# Day 16: Match Case Statements in Python 🐍

Welcome to Day 16 of the 100 Days of Python Challenge! Today, we will explore the `match` case statements introduced in Python 3.10. This feature allows for more readable and expressive code when dealing with multiple conditions.

## What are Match Case Statements? 🤔

The `match` case statement is similar to the `switch` case statements found in other programming languages. It allows you to match a value against a series of patterns and execute code based on which pattern matches.

## Example Code 📄

Here's an example of how to use `match` case statements with three different entities:

```python
def http_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

# Test the function
print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found
print(http_status(500))  # Output: Internal Server Error
print(http_status(123))  # Output: Unknown Status
```

In this example, the `http_status` function uses a `match` statement to return a message based on the provided status code.

## Attached Notes 📎

For more detailed notes and examples, please refer to the attached notes provided in this repository.

Happy coding! 🚀