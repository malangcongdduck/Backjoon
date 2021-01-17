n=int(input())
s=list(map(int,input().split()))
s.sort()

result=0

for i in s:
    true_p=1
    if i==1:
        continue
    elif i==2:
        pass
    else:
        for j in range(2,i):
            if i%j==0:
                true_p=0

    result+=true_p

print(result) 
