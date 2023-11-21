"""
ID: shane.t1
TASK: beads
LANG: PYTHON3
"""
def count_collectedbeads(necklace):
    n = len(necklace)
    necklace += necklace
    maxcount = 0
    for i in range(n):
        coulor1 = 'w'
        coulor2 = 'w'
        count1 = 0
        count2 = 0
        j = i
        while j >= 0:
            if coulor1 == 'w' and necklace[j] != 'w':
                coulor1 = necklace[j]
            if coulor1 == necklace[j] and necklace[j] != 'w':
                break
            count1 += 1
            j -= 1
        j = i + 1
        while j < n * 2:
            if coulor2 == 'w' and necklace[j] != 'w':
                coulor2 = necklace[j]
            if coulor2 == necklace[j] and necklace[j] != 'w':
                break
            count2 += 1
            j += 1
        maxcount = max(maxcount, min(count1 + count2, n))
    return maxcount


with open('beads.in', 'r')as file:
    n = int(file.readline().strip())
    necklace = file.readline().strip()

nemo = count_collectedbeads(necklace)

with open('beads.out', 'w')as file:
    file.write(str(nemo) + '\n')
        