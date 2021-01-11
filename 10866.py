from collections import deque
import sys

n=int(sys.stdin.readline())
q=deque()

for i in range(n):
    ord=sys.stdin.readline().split()

    if ord[0]=='push_front':
        q.appendleft(ord[1])
    elif ord[0]=='push_back':
        q.append(ord[1])
    elif ord[0]=='pop_front':
        if len(q)==0:
            print('-1')
        else:
            print(q.popleft())
    elif ord[0]=='pop_back':
        if len(q)==0:
            print('-1')
        else:
            print(q.pop())
    elif ord[0]=='size':
        print(len(q))
    elif ord[0]=='empty':
        if len(q)==0:
            print('1')
        else:
            print('0')
    elif ord[0]=='front':
        if len(q)==0:
            print('-1')
        else:
            print(q[0])
    elif ord[0]=='back':
        if len(q)==0:
            print('-1')
        else:
            print(q[len(q)-1])
