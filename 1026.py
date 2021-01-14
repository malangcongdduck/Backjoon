import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

a.sort()
result=[]
for i in range(n):
    result.append(a[i]*max(b))
    b.pop(b.index(max(b)))

print(sum(result))