import sys
n=int(sys.stdin.readline())
coin=[500,100,50,10,5,1]
m=1000-n
count=0

for i in coin:
    if m//i>0:
        count+=m//i
        m=m%i
            
print(count)