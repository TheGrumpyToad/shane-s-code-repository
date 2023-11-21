"""
ID: shane.t1
LANG: PYTHON3
PROG: milk
"""
def milk_maker(farmers, total_needed):
    farmers = sorted(farmers)
    total_price = 0
    for f in farmers:
        price = f[0]
        amt = f[1]
        if total_needed >= amt:
            total_price += price * amt
            total_needed -= amt
        else:
            total_price += total_needed * price
            break
    return total_price

with open('milk.in', 'r')as file:
    n, m = map(int, file.readline().split())
    farmers = []
    for i in range(m):
        price, amt = map(int, file.readline().split())
        farmers.append((price, amt))

result = milk_maker(farmers, n)

with open('milk.out', 'w')as file:
    file.write(str(result) + '\n')

