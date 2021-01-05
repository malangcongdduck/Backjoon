c=int(input())
b=[]

for i in range(c):
    n=list(map(int,input().split()))
    avg=sum(n[1:])/n[0]
    count=0
    percent=0

    for k in range(1, n[0]+1):
        if n[k]>avg:
            count+=1

    percent=count/n[0]*100
    b.append(percent)

for j in b:
    print('%.3f%%'%j)