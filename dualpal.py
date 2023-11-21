"""
ID: shane.t1
LANG: PYTHON3
PROG: dualpal
"""

def is_panidroms(base_str):
    return base_str == base_str[::-1]
def converte(cur_num, base):
    if cur_num == 0:
        return '0'
    symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    converted_number = ''
    while cur_num > 0:
        remainder = cur_num % base
        converted_number = symbols[remainder] + converted_number
        cur_num //= base
    return converted_number
def find_numbers(n, s):
    with open('dualpal.out', 'w')as out:
        already_found = 0
        cur_num = s + 1
        while already_found < n:
            n_palin = 0
            for base in range(2, 11):
                base_str = converte(cur_num, base)
                if is_panidroms(base_str):
                    n_palin += 1
                if n_palin >= 2:
                    break
            if n_palin >= 2:
                out.write(str(cur_num) + '\n')
                already_found += 1 
            cur_num += 1
with open('dualpal.in', 'r')as file:
    n, s = map(int, file.readline().split())
find_numbers(n, s)


