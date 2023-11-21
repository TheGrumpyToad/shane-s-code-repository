"""
ID: shane.t1
LANG: PYTHON3
PROG: wormhole
"""
with open('wormhole.in', 'r')as file:
    n = int(file.readline().strip())
    wormholes = [tuple(map(int, file.readline().split())) for _ in range(n)]
next_wormholes = {}
total_combinations = 0
for i in range(0, n):
    min_y = -1
    pair_idx = -1
    for j in range(0, n):
        if j != i and wormholes[i][1] == wormholes[j][1] and wormholes[i][0] < wormholes[j][0]:
             if wormholes[j][0] < min_y or min_y == -1:
                  min_y = wormholes[j][0]
                  pair_idx = j
    if pair_idx >= 0:
        next_wormholes[i] = pair_idx 
def check_loop(current_holes):
     # i decides which wormhole it should start on
     for i in range(n):
          visited = set()
          cur = current_holes[i]
          while True:
               if cur in visited:
                    return True
               visited.add(cur)
               # if the current wormhole has a wormhole to it's right:
               if cur in next_wormholes:
                    left = next_wormholes[cur]
                    # finds the paired wormhole of the next wormhole, breaks because you have already found the loop
                    for j in range(n):
                         if current_holes[j] == left:
                              break
                         # if the pair is not in the front, then it is in the back
                    if j % 2 == 0: 
                         cur = current_holes[j + 1]
                    else:
                         cur = current_holes[j - 1]
               else:
                    break
     return False
def all_possible_pairs(current_holes, n):
    global total_combinations
    if len(current_holes) == n:
        if check_loop(current_holes):
            total_combinations += 1
        return 
    for i in range(0, n):
           if not i in current_holes:
                # rule #1
                if len(current_holes) % 2 == 1 and i < current_holes[-1]:
                     continue
                if len(current_holes) % 2 == 0 and len(current_holes) >= 2 and i < current_holes[-2]:
                     continue
                all_possible_pairs(current_holes + [i], n)
all_possible_pairs([], n)
with open('wormhole.out', 'w')as file:
     file.write(str(total_combinations) + '\n')

