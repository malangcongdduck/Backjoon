#에라토스테네스의 체
import sys

m,n=map(int,sys.stdin.readline().split())
s=[False,False]+[True]*(n-1)

for i in range(2,n+1):
    if s[i]==True and i>=m:
        print(i)
    for j in range(2*i,n+1,i):
        if s[j]==True:
            s[j]=False