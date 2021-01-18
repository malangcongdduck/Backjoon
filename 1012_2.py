import sys
from collections import deque
t=int(sys.stdin.readline())

xx=[-1,1,0,0]
yy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    global n
    global m

    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            if n>y+yy[i]>=0 and m>x+xx[i]>=0:
                if G[y+yy[i]][x+xx[i]]==1:
                    q.append((x+xx[i],y+yy[i]))
                    G[y+yy[i]][x+xx[i]]=2


for i in range(t):
    m,n,k=map(int,sys.stdin.readline().split())


    #그래프 생성
    G=[[0]*m for i in range(n)]
    for _ in range(k):
        x,y=map(int,sys.stdin.readline().split())
        G[y][x]=1

    cnt=0
    for i in range(n):
        for j in range(m):
            if G[i][j]==1:
                cnt+=1
                G[i][j]=2
                bfs(j,i)


    print(cnt)