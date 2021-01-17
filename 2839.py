import sys
n=int(sys.stdin.readline())
count=0

while True:
    if n%5==0:
        count+=n//5
        break

    n-=3
    count+=1
    
    if n<0:
        count=-1
        break

print(count) 
