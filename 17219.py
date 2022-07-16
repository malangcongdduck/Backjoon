import sys

n, m = map(int, sys.stdin.readline().split())
dict = {}

for _ in range(n):
    url, pwd = sys.stdin.readline().split()
    dict[url] = pwd

for _ in range(m):
    print(dict[sys.stdin.readline().rstrip()])
