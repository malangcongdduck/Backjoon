n=int(input())
sum=0

if n==0:
    sum=0
elif n==1:
    sum=1
else:
    a=0
    b=1

    for i in range(2,n+1):
        sum=a+b
        a=b
        b=sum

print(sum) 
