import sys

def dfs(start,visited):
    if len(visited)==6:
        for i in visited:
            print(i, end=' ')
        print()
    
    else:
        for i in range(start,len(num)):
            if num[i] not in visited:
                dfs(i,visited+[num[i]])


while True:
    num=list(map(int,sys.stdin.readline().split()))

    if num[0]==0:
        break

    for i in range(1,len(num)-1):
       dfs(i,[num[i]])

    print()