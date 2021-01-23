import sys

def binary(first,end,target):
    mid=(first+end)//2
    
    while first<=end:
        if A[mid]==target:
            return 1
        elif A[mid]>target:
            return binary(first,mid-1,target)
        else:
            return binary(mid+1,end,target)

    return 0

n=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
check=list(map(int,sys.stdin.readline().split()))

A.sort()

for i in check:
    print(binary(0,n-1,i))