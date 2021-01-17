import sys 
from collections import deque

n,k=map(int,sys.stdin.readline().split())
q=deque()

for i in range(1,n+1):
    q.append(i)

ans=[]

while q:
    for _ in range(k-1):
        q.append(q.popleft())

    ans.append(q.popleft())

print('<',end='')
for i in range(len(ans)-1):
    print(ans[i],end=', ')
print(str(ans[-1])+'>')
