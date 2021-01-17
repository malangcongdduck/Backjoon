import sys
from collections import deque

n,k,m=map(int,sys.stdin.readline().split())
q=deque()

for i in range(1,n+1):
    q.append(i)

ans=[]
plag=1
while q:
    if plag==1:
        for _ in range(k-1):
            q.append(q.popleft())
        ans.append(q.popleft())
    elif plag==0:
        for _ in range(k-1):
            q.appendleft(q.pop())
        ans.append(q.pop())
     
    if len(ans)%m==0:
        if plag==1: 
            plag=0
        elif plag==0:
            plag=1

    

for i in ans:
    print(i)