"""
ID: shane.t1
LANG: PYTHON3
PROG: beads
"""
def count_collected_beads(necklace , n):
    n = len(necklace)
    necklace += necklace
    max_beads = 0
    for i in range(n):
        coulor1 = 'w'
        coulor2 = 'w'
        count1 = 0
        count2 = 0
        j = i
        while j >= 0:
            if coulor1 == 'w' and necklace[j] != 'w':
                coulor1 = necklace[j]
            if coulor1 != necklace[j] and necklace[j] != 'w':
                break
            count1 += 1
            j -= 1
        j = i + 1
        while j < n * 2:
            if coulor2 == 'w' and necklace[j] != 'w':
                coulor2 = necklace[j]
            if coulor2 != necklace[j] and necklace[j] != 'w':
                break
            count2 += 1
            j += 1
        max_beads = max(max_beads, min(count1 + count2, n))
    return max_beads
with open('beads.in', 'r')as file:
    n = file.readline().strip()
    necklace = file.readline().strip()
beny = count_collected_beads(necklace , n)
with open('beads.out', 'w')as file:
    file.write(str(beny) + '\n')
        
        