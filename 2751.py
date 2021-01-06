import sys
n=int(sys.stdin.readline())
a=[None]*n

for i in range(n):
    a[i] = int(sys.stdin.readline())

a.sort()

for i in a:
    print(i)