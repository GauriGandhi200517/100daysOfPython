x = int(input("enter the value of x:"))
match x:
    case 0:
        print("x is zero")
    case _ if x > 0:
        print("x is positive")
    case _:
        print("x is negative")
