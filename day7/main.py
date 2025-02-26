print(5+6)
print(15-6)
print(5*6)
print(15/6)
print(15//6)
print(15%6)
print(15**6)
print(15**0.5)
## Exercise 1 calculator using python
# Write a function that takes two numbers as arguments and return their sum, difference, product, division, floor division, and modulus.
def calculator(a, b):
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Example usage
calculator(16, 9)