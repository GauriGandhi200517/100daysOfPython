ep1 = {122:44, 122:56, 122:78, 122:89}
ep2 = {222:44, 222:99, 222:68, 222:60}
ep1.update(ep2) 
ep1.clear()
ep1.pop(122, None)
print(ep1)
