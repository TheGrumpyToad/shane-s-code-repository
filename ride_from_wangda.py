
"""
ID: shane.t1
LANG: PYTHON3
PROG: ride
"""

value = 1

file_path = "ride.in"  # Replace with the actual file path

with open(file_path, 'r') as file:
    line1 = file.readline()
    line2 = file.readline()

for i in line1:
	value *= ord(i) - ord('A') + 1

value = value % 47



valu = 1

for i in line2:
	valu *= ord(i) - ord('A') + 1
valu = valu % 47

file_path = "ride.out"  # Replace with the actual file path

with open(file_path, 'w') as file:
	if valu == value:
		file.write("GO")
	else:
		file.write("STAY")
	file.write('\n')
