
"""
ID: shane.t1
LANG: PYTHON3
PROG: palsquare
"""
def is_panidroms(s):
    return s == s[::-1]
def converte(num, base):
    if num == 0:
        return '0'
    symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    converted_number = ''
    while num > 0:
        remainder = num % base
        converted_number = symbols[remainder] + converted_number
        num //= base
    return converted_number
def get_all_panidroms(base):
    with open('palsquare.out', 'w')as file:
        for i in range(1, 300 + 1):
            s1 = converte(i, base)
            s2 = converte(i*i, base)
            if is_panidroms(s2):
                output = f'{s1} {s2}\n'
                file.write(output)
with open('palsquare.in','r')as file:
    base = int(file.readline().strip())
get_all_panidroms(base)
