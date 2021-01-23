import sys

def dfs(start,visited,summ):
    global cnt
    if summ==s:
        cnt+=1

    for i in range(start,n):
        if i not in visited:
            dfs(i,visited+[i],summ+li[i])

n,s=map(int,sys.stdin.readline().split())
li=list(map(int,sys.stdin.readline().split()))
cnt=0

for i in range(n):
    dfs(i,[i],li[i])

print(cnt)