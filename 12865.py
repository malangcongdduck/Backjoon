import sys

n,k=map(int,sys.stdin.readline().split())

stuff=[[0]*(k+1) for _ in range(n)]
for i in range(n):
    w,v=map(int,sys.stdin.readline().split())
    
    for j in range(1, k+1):
        if j>=w:
            stuff[i][j]=max(stuff[i-1][j],stuff[i-1][j-w]+v)
        else:
            stuff[i][j]=stuff[i-1][j] 

    #print(stuff)

print(max(stuff[-1]))