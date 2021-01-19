import sys

def dfs(visited):
    if len(visited)==m:
        for i in visited:
            print(i, end=' ')
        print()

    for i in range(1,n+1):
        if i not in visited:
            dfs(visited+[i])

n,m=map(int,sys.stdin.readline().split())

dfs([])