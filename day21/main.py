def average(a=9,b=4):
    print("the average is", (a+b)/2) 

    

def calculate_average(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)
      