"""
ID: shane.t1
TASK: milk2
LANG: PYTHON3
"""
def milk_2(n, intervals):
    intervals.sort()
    max_milking_time = 0
    max_idle_time = 0
    start, end = intervals[0]
    for i in range(n):
        intervals_start, intervals_end = intervals[i]
        if intervals_start <= end:
            end = max(end, intervals_end)
        else:
            milking_time = end - start
            idle_time = intervals_start - end
            max_milking_time = max(max_milking_time, milking_time)
            max_idle_time = max(max_idle_time, idle_time)
            start = intervals_start
            end = intervals_end
    milking_time = end - start
    max_milking_time = max(max_milking_time, milking_time)
    return max_milking_time, max_idle_time

with open('milk2.in', 'r')as file:
    n = int(file.readline().strip())
    intervals = []
    for _ in range(n):
        start, end = map(int, file.readline().split())
        intervals.append((start, end))

milk_time, idle_time = milk_2(n , intervals)

with open('milk2.out', 'w')as file:
    file.write(f'{milk_time}')