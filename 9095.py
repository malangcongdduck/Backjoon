import sys

t=int(sys.stdin.readline())
ans=[0]*20
ans[0]=0
ans[1]=1
ans[2]=2
ans[3]=4

def sum123(n):
    if n==1:
        return ans[1]
    elif n==2:
        return ans[2]
    elif n==3:
        return ans[3]
    elif ans[n]!=0:
        return ans[n]
    else:
        ans[n]=sum123(n-1)+sum123(n-2)+sum123(n-3)
        return ans[n] 


for i in range(t):
    n=int(sys.stdin.readline())
    print(sum123(n))
    print() 
