import sys
from collections import deque

xx=[-1,1,0,0]
yy=[0,0,-1,1]

def bfs(x,y):
    global n
    global m
    cnt=1
    q=deque()
    
    q.append((x,y,cnt))
    while q:
        x,y,cnt=q.popleft()
        if x==m-1 and y==n-1:
            return cnt

        for i in range(4):
            if m>x+xx[i]>=0 and n>y+yy[i]>=0:
                if G[y+yy[i]][x+xx[i]]==1:
                    q.append((x+xx[i],y+yy[i],cnt+1))
                    G[y+yy[i]][x+xx[i]]=2

    

n,m=map(int,sys.stdin.readline().split())
G=[[0]*m for _ in range(n)]

for i in range(n):
    map=list(sys.stdin.readline())
    for j in range(m):
        G[i][j]=int(map[j])


print(bfs(0,0))