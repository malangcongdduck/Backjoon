import sys

t = int(sys.stdin.readline())

for _ in range(t):
    blank = sys.stdin.readline()
    n = int(sys.stdin.readline())
    candy = [int(sys.stdin.readline()) for _ in range(n)]
    if sum(candy) % n == 0:
        print("YES")
    else:
        print("NO")
