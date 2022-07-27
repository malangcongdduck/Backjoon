import sys

n = int(sys.stdin.readline())
straws = [0] * n  # straw_1 = straw_2 /// straw_3
flag = 0

for i in range(n):
    straws[i] = int(sys.stdin.readline())

straws.sort(reverse=True)

for i in range(n-1):
    for j in range(i+1, n-1):
        if straws[j] + straws[j+1] > straws[i]:
            print(straws[j] + straws[j+1] + straws[i])
            flag = 1
            break

    if flag == 1:
        break

if flag == 0:
    print(-1)