import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    dq = deque()

    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    num.sort(reverse=True)

    for i in range(n):
        if i % 2 == 0:
            dq.append(num[i])
        else:
            dq.appendleft(num[i])

    dif = 0
    for i in range(n-1):
        if abs(dq[i] - dq[i+1]) > dif:
            dif = abs(dq[i] - dq[i+1])

    print(dif)
