from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())
s=list(map(int,sys.stdin.readline().split()))

q=deque([i for i in range(1, n+1)])
cnt2=0
cnt3=0

for i in s:
    index=q.index(i)

    if index<=(len(q)-1)//2:
        while q[0]!=i:
            q.append(q.popleft())
            cnt2+=1
        q.popleft()
    
    elif index>(len(q)-1)//2:
        while q[0]!=i:
            q.appendleft(q.pop())
            cnt3+=1
        q.popleft()

    #print(q)

print(cnt2+cnt3)
