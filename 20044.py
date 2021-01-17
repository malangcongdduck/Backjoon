n=int(input())
s=list(map(int,input().split()))
s.sort()

s_m=[] #역량리스트
t=2*n-1 #s의 역순 인덱스

for i in range(n):
    s_m.append(s[i]+s[t-i])

print(min(s_m)) 
