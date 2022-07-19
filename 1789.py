import sys

S = int(sys.stdin.readline())
N = 0
cal = 0

for i in range(1, S+1):
    cal += i
    N += 1
    if cal > S:
        N -= 1
        break

print(N)
