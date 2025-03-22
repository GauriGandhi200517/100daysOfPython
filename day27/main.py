question="WHO IS THE PRESIDENT OF INDIA?"
print(question)
options=["A.Dropadi MURMU","B. NARENDRA MODI","C. RAHUL GANDHI","D. MANMOHAN SINGH"]
for i in options:
    print(i)    
answer="A. Dropadi MURMU"
user_input = input("Enter your OPTION : ")    
if user_input == "A. Dropadi MURMU":
    print("CONGRATULATIONS! YOU ARE RIGHT.")
elif user_input == "B. NARENDRA MODI":
    print("SORRY! YOU ARE WRONG.")
elif user_input == "C. RAHUL GANDHI":
    print("SORRY! YOU ARE WRONG.")
elif user_input == "D. MANMOHAN SINGH":
    print("SORRY! YOU ARE WRONG.")
else:
    print("USER DO U WANT TO QUIT THE GAME?")