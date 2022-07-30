import sys

num = list(map(int, sys.stdin.readline().split()))
num.sort()

for i in range(1, num[0]*num[1]*num[2]+1):
    cnt = 0
    for j in num:
        if i % j == 0:
            cnt += 1

    if cnt > 2:
        print(i)
        break
