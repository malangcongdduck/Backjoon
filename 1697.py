import sys
from collections import deque
#0=방문안한 것
#1=방문한 것

def bfs(n):
    global k
    cnt=1
    q=deque()

    q.append((n,cnt))
    while q:
        n,cnt=q.popleft()
        if n==k:
            return cnt-1

        if 0<=n+1<=200000 and G[n+1]==0:
            q.append((n+1,cnt+1))
            G[n+1]=1
        if 0<=n-1<=200000 and G[n-1]==0:
            q.append((n-1,cnt+1))
            G[n-1]=1
        if 0<=n*2<=200000 and G[n*2]==0:
            q.append((n*2,cnt+1))
            G[n*2]=1

        #print(q)
        #print(n,cnt)
        #print()




n,k=map(int,sys.stdin.readline().split())

G=list(0 for i in range(200001))

print(bfs(n))