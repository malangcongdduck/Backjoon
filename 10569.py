import sys

t = int(sys.stdin.readline())

for i in range(t):
    v, e = map(int, sys.stdin.readline().split())
    print(2 - v + e)
