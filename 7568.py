n=int(input())
s=[]

for i in range(n):
    w,h=map(int,input().split())
    s.append((w,h))

for i in s:
    cnt=1
    for j in s:
        #자신보다 몸무게와 키가 큰 사람을 카운트
        if i[0]<j[0] and i[1]<j[1]:
            cnt+=1
    print(cnt, end=' ')