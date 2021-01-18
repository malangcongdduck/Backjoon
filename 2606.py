from collections import deque
import sys

#그래프 생성
n=int(sys.stdin.readline())#정점
m=int(sys.stdin.readline())#간선

G=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x,y=map(int,sys.stdin.readline().split())
    G[x][y]=1
    G[y][x]=1


q=deque()
visited=[]

#1번 컴퓨터가 웜 바이러스에 걸림
visited.append(1)
q.append(1)

while q:
    v=q.popleft()
    for i in range(1,n+1):
        if G[v][i]==1 and i not in visited:
            visited.append(i)
            q.append(i)

print(len(visited)-1) 
