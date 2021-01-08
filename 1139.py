n=int(input())
s=list(map(int,input().split()))
s.sort()

sum=0
for i in range(n):
    for j in range(i+1):
        sum+=s[j]

print(sum)