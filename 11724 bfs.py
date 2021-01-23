import sys
from collections import deque

def bfs():
    q=deque()
    cnt=0
    for i in range(1,n+1):
        if visited[i]==0:
            visited[i]=1
            q.append(i)
            cnt+=1
            while q:
                temp=q.popleft()
                for j in G[temp]:
                    if visited[j]==0:
                        q.append(j)
                        visited[j]=1
    
    return cnt

n,m=map(int,sys.stdin.readline().split())
G=[[] for _ in range(n+1)]
visited=[0]*(n+1)

for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    G[x].append(y)
    G[y].append(x)

print(bfs())