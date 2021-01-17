n=int(input())
s=list(map(int,input().split()))
s=set(s)

a=sorted(list(s))

for i in range(len(a)):
    print(f'{a[i]} ',end='') 
