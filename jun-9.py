input1 = 'ABCD'

output1 = []

for cat in input1:
    if cat.isalpha():
        output1.extend([cat, ord(cat.upper()) - ord('A') + 1])
print(output1)