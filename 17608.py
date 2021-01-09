import sys
n=int(sys.stdin.readline())
s=[None]*n

for i in range(n):
    s[i]=int(sys.stdin.readline())
    
max=s[n-1]
count=1
for i in range(n-2,-1,-1):
    if max<s[i]:
        max=s[i]
        count+=1

print(count)