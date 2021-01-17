a,b=list(map(str,input().split()))

a=a[::-1]
b=b[::-1]

a_m=int(a)
b_m=int(b)


if a_m>b_m:
    print(a_m)
else:
    print(b_m) 
