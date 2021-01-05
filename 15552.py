import sys
t=int(input())

for i in range(t):
    a,b=map(int,sys.stdin.readline().split(' '))#''단위로 리스트를 만들어서 n,m에 할당
    print(a+b)