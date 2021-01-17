import sys
from collections import deque

#그래프 생성
n=int(sys.stdin.readline())
G=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    ans=sys.stdin.readline()
    for j in range(1,n+1):
        G[i][j]=int(ans[j-1])

xx=[-1,1,0,0]
yy=[0,0,-1,1]

def dfs(x,y):
    cnt=1
    for i in range(4):
        if n>=x+xx[i]>0 and n>=y+yy[i]>0:
            if G[x+xx[i]][y+yy[i]]==1:
                G[x+xx[i]][y+yy[i]]=0
                cnt+=dfs(x+xx[i],y+yy[i])
    return cnt
    


result=[]#결과 배열
for i in range(1,n+1):
    for j in range(1,n+1):
        if G[i][j]!=0:
            G[i][j]=0
            result.append(dfs(i,j))

result.sort()
print(len(result))
for i in result:
    print(i)

