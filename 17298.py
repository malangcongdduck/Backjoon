import sys
from collections import deque

n=int(sys.stdin.readline())
seq_li=list(map(int,sys.stdin.readline().split()))
q=deque()
ans=deque()

for i in range(n-1,-1,-1):
    while q:
        if q[-1]<=seq_li[i]:
            q.pop()
        else:
            ans.appendleft(q[-1])
            q.append(seq_li[i])
            break

    if len(q)==0:
        ans.appendleft(-1)
        q.append(seq_li[i])

#print(q)
for i in ans:
    print(i,end=' ') 
