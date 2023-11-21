
"""
ID: shane.t1
LANG: PYTHON3
PROG: namenum
"""
def load_dictionary(filename):
    with open(filename, 'r') as f:
        return set(line.strip() for line in f)

def number_to_name(number):
    mappings = {
        '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
        '6': 'MNO', '7': 'PRS', '8': 'TUV', '9': 'WXY'
    }
    names = ['']
    for digit in number:
        letters = mappings.get(digit, '')
        names = [name + letter for name in names for letter in letters]
    return names

def find_valid_names(number, dictionary):
    possible_names = number_to_name(number)
    valid_names = [name for name in possible_names if name in dictionary]
    return valid_names

# Main program
number = input().strip()
dictionary = load_dictionary('dict.txt')
valid_names = find_valid_names(number, dictionary)

output_filename = "valid_names.txt"
with open(output_filename, 'w') as f:
    if valid_names:
        for name in valid_names:
            f.write(name + '\n')
    else:
        f.write("NONE\n")