"""
ID: shane.t1
LANG: PYTHON3
PROG: barn1
"""
with open('barn1.in')as file:
    n, s, c = map(int, file.readline().split())
    stalls = [0 for _ in range(s)]
    if c == 0:
        exit(0)
    for _ in range(c):
        pos = int(file.readline().strip())
        stalls[pos - 1] = 1
    gaps = []
    i = 0
for cow_start in range(len(stalls)):
    if stalls[cow_start] == 1:
        break
for cow_end in range(len(stalls)-1,-1,-1):
    if stalls[cow_end] == 1:
        break
spam = cow_end - cow_start + 1
while i < len(stalls):
    if i > 0 and stalls[i - 1] == 1 and stalls[i] == 0:
        n_empty_stalls = 0
        while i < len(stalls) and stalls[i] == 0:
            n_empty_stalls += 1
            i += 1
        if i < len(stalls):
            gaps.append(n_empty_stalls)
    else:
        i += 1
gaps = sorted(gaps)[::-1]
for i in range(min(n - 1, len(gaps))):
    spam -= gaps[i]
with open('barn1.out', 'w')as file:
    file.write(str(spam) + '\n')
    
    
