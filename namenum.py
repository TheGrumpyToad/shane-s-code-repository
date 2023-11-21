"""
ID: shane.t1
LANG: PYTHON3
PROG: namenum
"""
def recursive(dicts, code, current_name, brand_number, output_file, indx):
    if indx == len(brand_number):
        if current_name in dicts:
            output_file.write(str(current_name) + '\n')
            return True
    else:
        found = False
        for i in code[brand_number[indx]]:
            if recursive(dicts, code, current_name + i, brand_number, output_file, indx + 1):
                found = True
        return found


code = {"2": 'ABC',     "5": 'JKL',     "8": 'TUV',
         "3": 'DEF' ,   "6": 'MNO'  ,  "9": 'WXY' ,
         "4": 'GHI' ,    "7":'PRS'}

dicts = set()

with open('dict.txt', 'r')as file:
    for line in file:
        dicts.add(line.strip())

with open('namenum.in', 'r')as file:
    brand_number = file.readline().strip()

with open('namenum.out', 'w')as file:
    if not recursive(dicts, code, '', brand_number, file, 0):
        file.write('NONE\n')