import sys

def dfs(visited):
    if len(visited)==m:
        for i in visited:
            print(i, end=' ')
        print()

    else:
        for i in range(1,n+1):
            dfs(visited+[i])


n,m=map(int,sys.stdin.readline().split())
dfs([])