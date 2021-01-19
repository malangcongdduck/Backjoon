import sys

def dfs(visited,num):
    if len(visited)==m:
        for i in visited:
            print(i, end=' ')
        print()

    else:
        for i in range(num,n+1):
            dfs(visited+[i], i)

n,m=map(int,sys.stdin.readline().split())
dfs([],1)