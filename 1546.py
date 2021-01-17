n=int(input())
a=[None]*n
a=list(map(int,input().split()))

m=max(a)
result=0

for i in range(n):
    a[i]=a[i]/m*100
    result+=a[i]

result=result/n
=======
n=int(input())
a=[None]*n
a=list(map(int,input().split()))

m=max(a)
result=0

for i in range(n):
    a[i]=a[i]/m*100
    result+=a[i]

result=result/n

print(result)
