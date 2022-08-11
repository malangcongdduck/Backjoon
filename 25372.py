import sys

n = int(sys.stdin.readline())

for _ in range(n):
    pwd = list(sys.stdin.readline().rstrip())
    print("yes" if 6 <= len(pwd) <= 9 else "no")
