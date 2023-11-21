"""
ID: shane.t1
TASK: crypt1
LANG: PYTHON3
# """
def validate_num(num, n_digits , digits):
    num_str = str(num)
    if len(num_str) != n_digits:
        return False
    for digit in num_str:
        if int(digit) not in digits:
            return False
    return True
with open('crypt1.in', 'r') as file:
    n_digits = file.readline().strip()
    line = file.readline()
    digits = [int(a) for a in line.split()]
n_solutions = 0
for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                for e in digits:
                    x = (a * 100 + b * 10 + c) * e
                    if not validate_num(x, 3, digits):
                         continue
                    y = a * 100 * d + b * 10 * d + c * d
                    if not validate_num(y, 3, digits):
                        continue
                    z = x + y * 10
                    if not validate_num(z, 4, digits):
                        continue
                    n_solutions += 1

with open('crypt1.out', 'w') as file:
    file.write(str(n_solutions) + '\n')



