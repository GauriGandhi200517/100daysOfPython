# exercise 2:code on greeting sir or madam 

import time
t=time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(hour)
if hour > 0 and hour < 12:
    print("Good Morning Sir/Madam!")
elif hour>=12 and hour<17:
    print("Good Afternoon Sir/Madam!")
else:
    print("Good night Sir/Madam!")    