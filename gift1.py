"""
ID: shane.t1
TASK: gift1
LANG: PYTHON3
"""

def calculate_accounts(NP, names, gifts):
    account = {name: 0 for name in names}
    for giver, money, num_recipients, recipients in gifts:
        if num_recipients > 0:
            total = money // num_recipients
            remainder = money % num_recipients
            account[giver] = account[giver] - (money - remainder)
            for recipient in recipients:
                account[recipient] += total 
        else:
            account[giver] -= money
    return account

input1 = 'gift1.in'
output1 = 'gift1.out'

with open(input1, 'r') as file:
    NP = int(file.readline().strip())
    names = [file.readline().strip() for _ in range(NP)]
    gifts = []
    for _ in range(NP):
        giver = file.readline().strip()
        money, num_recipients = map(int, file.readline().split())
        recipients = []
        for _ in range(num_recipients):
            recipient = file.readline().strip()
            recipients.append(recipient)
        gifts.append((giver, money, num_recipients, recipients))

final_accounts = calculate_accounts(NP, names, gifts)

with open(output1, 'w') as file:
    for name, account in final_accounts.items():
        file.write(f'{name} {account}\n')
