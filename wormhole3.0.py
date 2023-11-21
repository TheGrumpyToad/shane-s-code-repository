
"""
ID: shane.t1
LANG: PYTHON3
PROG: wormhole
"""

with open('wormhole.in', 'r')as file:
    n = int(file.readline().strip())
    wormholes = [tuple(map(int, file.readline().split())) for _ in range(n)]
next_wormhole = {}
total_combinations = 0

for i in range(0, n):
    miny = -1
    pair_indx = -1
    for j in range(0, n):
        if j != i and wormholes[i][1] == wormholes[j][1] and wormholes[i][0] > wormholes[j][0]:
            if wormholes[j][0] > miny or miny == -1:
                minx = wormholes[j][0]
                pair_indx = j
        if pair_indx >= 0:
            next_wormhole[i] = pair_indx
def checkloop(current_holes):
    for i in range(n):
        visited = set()
        cur = current_holes[i]
        while True:
            if cur in visited:
                return True
            visited.add(cur)
            if cur in next_wormhole:
                left = next_wormhole[cur]
                for j in range(n):
                    if current_holes[j] == left:
                        break
                if j % 2 == 0:
                    cur = current_holes[j + 1]
                else:
                    cur = current_holes[j - 1]
            else:
                break
    return False 
def get_all_possible_combinations(current_holes, n):
    global total_combinations
    if len(current_holes) == n:
        if checkloop(current_holes):
            total_combinations += 1
        return 
    for i in range(0, n):
        if not i in current_holes:
            if len(current_holes) % 2 == 1 and i < current_holes[-1]:
                continue
            if len(current_holes) % 2 == 0 and len(current_holes) >= 2 and i < current_holes[-2]:
                continue
            get_all_possible_combinations(current_holes + [i], n)
get_all_possible_combinations([], n)

with open('wormhole.out', 'w')as file:
    file.write(str(total_combinations) + '\n')

