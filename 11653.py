n=int(input())
a=2 #소수 시작

if n==1:
    pass
else:
    while n>=a:
        if n%a==0:
            print(a)
            n=n/a
        else:
            a+=1