from collections import deque
import sys
n,m,v=map(int,sys.stdin.readline().split())

#그래프 생성
G=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    G[a][b]=1
    G[b][a]=1

def dfs(visited,v):
    visited.append(v)
    for i in range(1,n+1):
        if G[v][i]==1 and i not in visited:
            visited=dfs(visited, i)
    return visited
            
def bfs(v):
    q=deque()
    visited=[]

    visited.append(v)
    q.append(v)
    while q:
        if len(visited)==n:
            break

        v=q.popleft()
        for i in range(1,n+1):
            if G[v][i]==1 and i not in visited:
                visited.append(i)
                q.append(i)

    return visited

print(*dfs([],v))
print(*bfs(v)) 
