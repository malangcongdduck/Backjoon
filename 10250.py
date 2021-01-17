t=int(input())

for i in range(t):
    h,w,n=map(int,input().split())

    if n%h==0:
        h_n=h
        w_n=n//h
    else:
        h_n=n%h
        w_n=n//h+1

    if 1<=w_n<=9: 
        print(str(h_n)+'0'+str(w_n))
    else:
        print(str(h_n)+str(w_n))
