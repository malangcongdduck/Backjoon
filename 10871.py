n,x=map(int,input().split())
a=[None]*n

a=list(map(int,input().split()))

for i in range(n):
    if a[i]<x:
        print(f'{a[i]} ',sep='',end='')