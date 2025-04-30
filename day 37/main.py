def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("enter an index:"))
        print(l[i])
        return 1
    except Exception as e:
        print("Some error occurred:", e)
        return 0
    finally:
        print("This will always execute")   
x=func1()
print(x)