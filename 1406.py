import sys
from collections import deque

sen = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
q = deque()
temp = deque()

for i in sen:
    q.append(i)


count = 0
cursor = len(q)
while count != n:
    commend = list(sys.stdin.readline().split())

    if commend[0] == 'P':
        q.append(commend[1])

    elif commend[0] == 'L':
        cursor = len(q)
        if cursor != 0:
            temp.append(q.pop())

    elif commend[0] == 'B':
        if len(q) != 0:
            q.pop()

    elif commend[0] == 'D':
        cursor = len(temp)
        if cursor != 0:
            q.append(temp.pop())

    count += 1


if len(temp) != 0:
    for i in range(len(temp)):
        q.append(temp.pop())

for i in q:
    print(i, end='')
