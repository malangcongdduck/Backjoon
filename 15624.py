import sys

n=int(sys.stdin.readline())

result=0
a=0
b=1

if n==0:
    print(result)
elif n==1:
    print(b)
else:
    for i in range(n-1):
        result=(a+b)%1000000007
        a=b
        b=result

    print(result) 
