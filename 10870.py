import sys
ans=[0]*100
ans[0]=0
ans[1]=1

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif ans[n]!=0:
        return ans[n]
    else:
        ans[n]=fibonacci(n-1)+fibonacci(n-2)
        return ans[n]

n=int(sys.stdin.readline())
print(fibonacci(n)) 
