# Day 15 of 100 Days of Python Challenge 🚀

Welcome to Day 15 of the 100 Days of Python Challenge! Today, we will be exploring the `time` module in Python. ⏰

## Exercise: Using the `time` Module

In this exercise, you will learn how to use the `time` module to work with time-related functions in Python. The `time` module provides various time-related functions, such as getting the current time, measuring the time taken by a code segment, formatting time, and more.

### Example Code

Here is an example code snippet that demonstrates the use of the `time` module:

```python
import time

# Get the current time
current_time = time.time()
print(f"Current Time (in seconds since epoch): {current_time}")

# Measure the time taken by a code segment
start_time = time.time()
# Simulate a delay
time.sleep(2)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")

# Format the current time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time))
print(f"Formatted Current Time: {formatted_time}")
```

### Explanation

1. **Getting the Current Time**: The `time.time()` function returns the current time in seconds since the epoch (January 1, 1970, 00:00:00 UTC).
2. **Measuring Elapsed Time**: By capturing the start and end times around a code segment, you can measure the time taken by that segment. The `time.sleep(2)` function is used to simulate a delay of 2 seconds.
3. **Formatting Time**: The `time.strftime()` function formats a time tuple to a readable string. In this example, `time.localtime(current_time)` converts the current time to a time tuple, and `%H:%M:%S"` specifies the format.

Feel free to experiment with the `time` module and explore its various functions. 


Happy coding! 🎉
