"""
ID: shane.t1
LANG: PYTHON3
PROG: combo
"""
def check_position(actual, expected, n):
    for i in range(0, 3):
        t = expected + i
        if t > n:
            t = t - n
        if actual == t: 
            return True
    for i in range(1, 3):
        t = expected - i
        if t < 1:
            t = t + n
        if actual == t:
            return True
    return False

    
def check_combination(a, b, c, combination, n):
    if check_position(a, combination[0], n) and check_position(b, combination[1], n) and check_position(c, combination[2], n):
        return True
    return False


with open('combo.in', 'r') as file:
    n = int(file.readline().strip())
    master = list(map(int, file.readline().split()))
    farmer = list(map(int, file.readline().split()))


n_solutions = 0
n_inner_loop_run = 0
for a in range(1, n + 1):
    if check_position(a, farmer[0], n) or check_position(a, master[0], n):
        for b in range(1, n + 1):
            if check_position(b, farmer[1], n) or check_position(b, master[1], n):
                for c in range(1, n + 1):
                    n_inner_loop_run += 1
                    if check_position(c, farmer[2], n) or check_position(c, master[2], n):
                        if check_combination(a, b, c, master, n) or check_combination(a, b, c, farmer, n):
                            n_solutions += 1
print(n_inner_loop_run)
with open('combo.out', 'w') as file:
    file.write(str(n_solutions) + '\n')
