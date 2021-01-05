<<<<<<< HEAD
n=int(input())
a=[None]*n

a=list(map(int,input().split()))

min=a[0]
max=a[0]

for i in range(1,n):
    if min>a[i]:
        min=a[i]
    if max<a[i]:
        max=a[i]

=======
n=int(input())
a=[None]*n

a=list(map(int,input().split()))

min=a[0]
max=a[0]

for i in range(1,n):
    if min>a[i]:
        min=a[i]
    if max<a[i]:
        max=a[i]

>>>>>>> e0846c0484c6df47787461a9982e06dbe6ae4039
print(f'{min} {max}')