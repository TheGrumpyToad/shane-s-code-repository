"""
ID: shane.t1
TASK: friday
LANG: PYTHON3
"""
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

def count_fridays(N):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_day_counts = [0] * 7
    current_weekday = 0
    for year in range(1900, 1900 + N):
        for month in range(12):
            if month == 1 and is_leap_year(year):
                month_days[1] = 29
            else:
                month_days[1] = 28
            for day in range(1, month_days[month] + 1):
                if day == 13:
                    week_day_counts[current_weekday] += 1
                current_weekday = (current_weekday + 1) % 7
    return week_day_counts

with open("friday.in", "r") as file:
    N = int(file.readline().strip())

result = count_fridays(N)

result = result[-2:] + result[:-2]

with open("friday.out", "w") as file:
    file.write(" ".join(map(str, result)))
    file.write("\n")