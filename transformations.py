"""
ID: shane.t1
LANG: PYTHON3
PROG: transform
"""
def rotate_90(pattern):
    n = len(pattern)
    rotated = [[''] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = pattern[i][j]
    return rotated


def rotate_180(pattern):
    return rotate_90(rotate_90(pattern))

def rotate_270(pattern):
    return rotate_90(rotate_180(pattern))

def reflect(pattern):
    return [row[::-1] for row in pattern]

def is_same(pattern1, pattern2):
    return pattern1 == pattern2

def transform(pattern1, pattern2):
    if rotate_90(pattern1) == pattern2:
        return 1
    elif rotate_180(pattern1) == pattern2:
        return 2
    elif rotate_270(pattern1) == pattern2:
        return 3
    elif reflect(pattern1) == pattern2:
        return 4
    elif rotate_90(reflect(pattern1)) == pattern2 or rotate_180(reflect(pattern1)) == pattern2 or rotate_270(reflect(pattern1)) == pattern2:
        return 5
    elif pattern1 == pattern2:
        return 6
    else: 
        return 7

def transfor(input_file, output_file):
    with open(input_file, 'r') as fin, open(output_file, 'w')as fout:
        n = int(fin.readline().strip())
        before = [list(fin.readline().strip() for _ in range(n))]
        after = [list(fin.readline().strip() for _ in range(n))]
        transformationss = transform(before, after)
        fout.write(str(transformationss) + '\n')
transfor('transform.in', 'transform.out')
