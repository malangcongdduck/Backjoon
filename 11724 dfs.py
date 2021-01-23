import sys
sys.setrecursionlimit(100000)

def dfs(start,visited):
    check[start]=1
    for i in range(len(G[start])):
        if G[start][i] and G[start][i] not in visited:
            dfs(G[start][i],visited+[G[start][i]])


n,m=map(int,sys.stdin.readline().split())
G=[[] for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    G[x].append(y)
    G[y].append(x)

cnt=0
check=[0]*(n+1)
for i in range(1,n+1):
    if check[i]==0:
        cnt+=1
        dfs(i,[i])
    #print(check)

print(cnt)