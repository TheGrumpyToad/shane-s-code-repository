value = 1

for i in input():
	value *= ord(i) - ord('A') + 1
print(value)

value = 1

valu = 1

for i in input():
	valu *= ord(i) - ord('A') + 1
print(valu)
print(valu % 47)
valu = 1

if valu == value:
	print("GO")
else:
	print("STOP")