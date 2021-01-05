a=[None]*9

for i in range(9):
    a[i]=int(input())

max=0

for i in range(9):
    if a[max]<a[i]:
        max=i

print(f'{a[max]}\n{max+1}')