<<<<<<< HEAD
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
>>>>>>> e0846c0484c6df47787461a9982e06dbe6ae4039
print(result)