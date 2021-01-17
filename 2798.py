import sys

n,m=map(int,sys.stdin.readline().split())
card=list(map(int,sys.stdin.readline().split()))
max=min(card)

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k]<=m and card[i]+card[j]+card[k]>=max:
                max=card[i]+card[j]+card[k]

print(max) 
