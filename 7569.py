import sys
from collections import deque

xx=[-1,1,0,0,0,0]
yy=[0,0,-1,1,0,0]
zz=[0,0,0,0,1,-1]

def bfs(box):
    q=deque(box)
    global m
    global n
    global h
    global tomato
    cnt=len(box)

    while q:
        x,y,z,day=q.popleft()
        for i in range(6):
            if n>y+yy[i]>=0 and m>x+xx[i]>=0 and h>z+zz[i]>=0:
                if G[z+zz[i]][y+yy[i]][x+xx[i]]==0:
                    q.append((x+xx[i],y+yy[i],z+zz[i],day+1))
                    G[z+zz[i]][y+yy[i]][x+xx[i]]=1
                    cnt+=1

                    if tomato==cnt:
                        return day+1
        
    if tomato==cnt:
        return 0
    else:
        return -1


m,n,h=map(int,sys.stdin.readline().split())
G=[[[0]*m for _ in range(n)]for _ in range(h)]
box=deque()

for k in range(h):
    for i in range(n):
        map=list(sys.stdin.readline().split())
        for j in range(m):
            G[k][i][j]=int(map[j])


#print(G)
tomato=0
day=0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if G[k][i][j]==1:
                box.append((j,i,k,0))
            if G[k][i][j]!=-1:
                tomato+=1

print(bfs(box))