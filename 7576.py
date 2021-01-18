import sys
from collections import deque

xx=[-1,1,0,0]
yy=[0,0,-1,1]

def bfs(box):
    q=deque(box)
    global m
    global n
    global tomato
    cnt=len(box)

    while q:
        x,y,day=q.popleft()
        for i in range(4):
            if n>y+yy[i]>=0 and m>x+xx[i]>=0:
                if G[y+yy[i]][x+xx[i]]==0:
                    q.append((x+xx[i],y+yy[i],day+1))
                    G[y+yy[i]][x+xx[i]]=1
                    cnt+=1

                    if tomato==cnt:
                        return day+1
        
    if tomato==cnt:
        return 0
    else:
        return -1


m,n=map(int,sys.stdin.readline().split())
G=[[0]*m for _ in range(n)]
box=deque()

for i in range(n):
    map=list(sys.stdin.readline().split())
    for j in range(m):
        G[i][j]=int(map[j])


tomato=0
day=0
for i in range(n):
    for j in range(m):
        if G[i][j]==1:
            box.append((j,i,0))
        if G[i][j]!=-1:
            tomato+=1

print(bfs(box)) 
