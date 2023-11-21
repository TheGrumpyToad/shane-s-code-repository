"""
ID: shane.t1
TASK: ride
LANG: PYTHON3
"""

def calculate_number(name):
    value = 1
    for i in name:
        value *= ord(i) - ord('A') + 1
    return value

with open('ride.in', 'r')as file:
    line = file.readlines()
    comet = line[0].strip()
    group = line[1].strip()

comet_ = calculate_number(comet)
group_ = calculate_number(group)

if comet_ % 47 == group_ % 47:
    result = 'GO'
else:
    result = 'STAY'

with open('ride.out','w') as file:
    file.write(result)
    file.write('\n')

