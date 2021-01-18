ans=[[0 for j in range(14)] for i in range(15)]
for i in range(15):
    ans[i][0]=1
for j in range(14):
    ans[0][j]=j+1
for i in range(1,15):
    for j in range(1,14):
        ans[i][j]=ans[i][j-1]+ans[i-1][j]

t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    print(ans[k][n-1])
