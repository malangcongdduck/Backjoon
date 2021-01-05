<<<<<<< HEAD
a=[None]*9

for i in range(9):
    a[i]=int(input())

max=0

for i in range(9):
    if a[max]<a[i]:
        max=i

=======
a=[None]*9

for i in range(9):
    a[i]=int(input())

max=0

for i in range(9):
    if a[max]<a[i]:
        max=i

>>>>>>> e0846c0484c6df47787461a9982e06dbe6ae4039
print(f'{a[max]}\n{max+1}')