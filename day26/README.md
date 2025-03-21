# Day 26: 100 Days of Python Challenge 🚀  

## Exercise 2: Greeting Sir or Madam 👋  

In this exercise, we created a Python program that greets the user based on the current time of the day. The program uses the `time` module to fetch the current hour and displays an appropriate greeting.  

### Code: 🖥️  
```python  
import time  
t = time.strftime("%H:%M:%S")  
hour = int(time.strftime("%H"))  
print(hour)  
if hour > 0 and hour < 12:  
    print("Good Morning Sir/Madam! 🌅")  
elif hour >= 12 and hour < 17:  
    print("Good Afternoon Sir/Madam! ☀️")  
else:  
    print("Good night Sir/Madam! 🌙")  
```  

### Explanation: 📖  
1. The `time.strftime("%H:%M:%S")` function retrieves the current time in hours, minutes, and seconds.  
2. The `hour` variable extracts the hour part of the current time.  
3. Based on the hour, the program determines whether it is morning, afternoon, or night and prints the corresponding greeting.  

### Output Example: 📝  
- If the current time is 10:00 AM, the output will be:  
  ```  
  10  
  Good Morning Sir/Madam! 🌅  
  ```  
- If the current time is 3:00 PM, the output will be:  
  ```  
  15  
  Good Afternoon Sir/Madam! ☀️  
  ```  
- If the current time is 9:00 PM, the output will be:  
  ```  
  21  
  Good night Sir/Madam! 🌙  
  ```  

This exercise demonstrates the use of Python's `time` module and conditional statements to create a dynamic greeting program. 🎉  

Happy Coding! 😊  