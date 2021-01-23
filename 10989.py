import sys

n=int(sys.stdin.readline())
n_list=[0]*10001 #계수정렬

for i in range(n):
    num=int(sys.stdin.readline())
    n_list[num]+=1

for i in range(len(n_list)):
    if n_list[i]!=0:
        for _ in range(n_list[i]):
            print(i)