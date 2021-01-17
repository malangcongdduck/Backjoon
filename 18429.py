import sys
n,k=map(int,sys.stdin.readline().split())
s=list(map(int,sys.stdin.readline().split()))

#375
def dfs(visited, kg, day):
    global count
    if day==n:
        count+=1 

    for i in range(n):
        if kg+s[i]-k>=500:
            if i not in visited:
                dfs(visited+[i],kg+s[i]-k, day+1)
          
count=0
dfs([],500,0) 
print(count)
