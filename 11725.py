import sys
from collections import deque

def bfs(start):
    q.append(start)

    while q:
        temp=q.popleft()
        for i in G[temp]:
            p[i]=temp
            q.append(i)
            G[i].remove(temp)

#G=[[],[6,4],[4],[6,5],[1,2,7],[3],[1,3],[4]]

n=int(sys.stdin.readline())
G=[[] for _ in range(n+1)]
p=[0 for _ in range(n+1)]
q=deque()

for i in range(n-1):
    x,y=map(int,sys.stdin.readline().split())
    G[x].append(y)
    G[y].append(x)

bfs(1)

for i in range(2,n+1):
    print(p[i])