import sys
n,k=map(int,sys.stdin.readline().split())
coin=[]

for i in range(n):
    coin.append(int(sys.stdin.readline()))

coin.reverse()
cnt=0

for i in coin:
    if k==0:
        break
    
    if i>k:
        continue
    else:
        cnt+=k//i
        k%=i
 
print(cnt)
