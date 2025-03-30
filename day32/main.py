s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1,s2)
for symmetric_difference in s1.symmetric_difference(s2):
	print(symmetric_difference)
print(s1 .issuperset(s2))
print(s1.issubset(s2))