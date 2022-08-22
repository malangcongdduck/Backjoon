import sys

n = int(sys.stdin.readline())
firm = dict()

for _ in range(n):
    name, state = sys.stdin.readline().split()

    if state == 'enter':
        firm[name] = 1
    elif state == 'leave':
        firm[name] = 0

firm = sorted(firm.items(), reverse=True)

for person in firm:
    if person[1] == 1:
        print(person[0])
